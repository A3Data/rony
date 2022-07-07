import yaml
from datetime import datetime

from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as f

from .data_quality import DataQuality

from pydeequ.analyzers import (
    AnalysisRunner, AnalyzerContext,
    ApproxCountDistinct, ApproxQuantile, ApproxQuantiles,
    Completeness, Compliance, Correlation, CountDistinct,
    DataType, Distinctness, Entropy, Histogram, KLLParameters, KLLSketch,
    Maximum, MaxLength, Mean, Minimum, MinLength, MutualInformation,
    PatternMatch, Size, StandardDeviation, Sum, Uniqueness,
    UniqueValueRatio
)


class Analyzer(DataQuality):
    """
    Class for building and running Analyzer jobs and output tables.

    Parameters
    ----------
    spark: SparkSession
        A SparkSession object
    """

    def __init__(self, spark: SparkSession) -> None:
        super().__init__(spark)


    def _analysis_job_builder(self, config_path: str) -> str:
        """
        Build the Analyzer job code as a string expression to be evaluated.

        Parameters
        ----------
        config_path: str
            Path to a yaml config file.
            Config file must have 2 major keys: columns and metrics.

            Columns major key must have dataframe column names as keys and lists of
            analysis methods as values (as each method listed here works with only one column as input).

            Methods major key was built to deal with methods that take more than one column or parameter.
            Methods major key must have methods as keys and lists of lists as values.

        YAML Example
        ------------

        columns:
            PassengerId: [Completeness]
            Age: [Completeness, Mean, StandardDeviation, Minimum, Maximum, Sum, Entropy]
            Sex: [Completeness, ApproxCountDistinct, Distinctness]
            Fare: [Completeness, Mean, StandardDeviation]
            Pclass: [DataType]
            Survived: [Histogram]
            Name: [MaxLength, MinLength]
        metrics:
            Correlation: 
                - [Fare, Age]
                - [Fare, Survived]
            Compliance: 
                - [Age, "Age>40.2"]
            PatternMatch: 
                - [Name, "M(r|rs|iss)."]
            ApproxQuantiles: 
                - [Age, '0.5', '0.25', '0.75']
                - [Fare, '0.5', '0.25', '0.75']
            Uniqueness:
                - [PassengerId]
                - [Name,Sex]
                - [Ticket]
            UniqueValueRatio:
                - [PassengerId]
                - [Name,Sex]

        Returns
        -------
        str -> The AnalysisRunner expression as a str object
        """
        with open(config_path, "r") as file:
            configurations = yaml.full_load(file)

        columnsconfig = configurations["columns"]
        metricsconfig = configurations["metrics"]

        expression = "AnalysisRunner(spark).onData(df).addAnalyzer(Size())"

        for col in columnsconfig.keys():
            for method in columnsconfig[col]:
                expression += ".addAnalyzer(" + method + '("' + col + '"))'

        for method in metricsconfig.keys():

            for params in metricsconfig[method]:
                expression += ".addAnalyzer(" + method + '('
            
                if method == "ApproxQuantiles":
                    expression += '"' + params[0] + '", [' 
                    for i in range(1,len(params)):
                        expression += params[i] + ', '
                    expression += ']'
                
                elif method == "ApproxQuantile":
                    expression += '"' + params[0] + '", ' + params[1]

                elif method == "Uniqueness" or method == "UniqueValueRatio":
                    expression += '[' 
                    for i in range(len(params)):
                        expression += '"' + params[i] + '", '
                    expression += ']'

                else:
                    for col in params:
                        expression += '"' + col + '", '
                expression += '))'

        expression += ".run()"
        return expression


    def run(self, df: DataFrame, config: str) -> DataFrame:
        """
        Run the Analyzer job

        Parameters
        ----------

        df: DataFrame
            A Spark DataFrame

        config: str
            Path to a yaml config file or a str expression of AnalysisRunner to evaluate.

            If config is a path to a yaml file, config file must have 2 major keys: columns and metrics.

            Columns major key must have dataframe column names as keys and lists of
            analysis methods as values (as each method listed here works with only one column as input).

            Methods major key was built to deal with methods that take more than one column or parameter.
            Methods major key must have methods as keys and lists of lists as values.

        YAML Example
        ------------

        columns:
            PassengerId: [Completeness]
            Age: [Completeness, Mean, StandardDeviation, Minimum, Maximum, Sum, Entropy]
            Sex: [Completeness, ApproxCountDistinct, Distinctness]
            Fare: [Completeness, Mean, StandardDeviation]
            Pclass: [DataType]
            Survived: [Histogram]
            Name: [MaxLength, MinLength]
        metrics:
            Correlation: 
                - [Fare, Age]
                - [Fare, Survived]
            Compliance: 
                - [Age, "Age>40.2"]
            PatternMatch: 
                - [Name, "M(r|rs|iss)."]
            ApproxQuantiles: 
                - [Age, '0.5', '0.25', '0.75']
                - [Fare, '0.5', '0.25', '0.75']
            Uniqueness:
                - [PassengerId]
                - [Name,Sex]
                - [Ticket]
            UniqueValueRatio:
                - [PassengerId]
                - [Name,Sex]

        Returns
        -------

        DataFrame -> A DataFrame with the results for Analyzer job.
        """
        try:
            expression = self._analysis_job_builder(config)
        except:
            expression_start = "AnalysisRunner(spark).onData(df)"
            if not config.startswith(expression_start):
                raise AttributeError("String expression should start with 'AnalysisRunner(spark).onData(df)'")
            else:
                expression = config

        spark = self.spark
        analysisResult = eval(expression)

        analysisResult_df = (
            AnalyzerContext
                .successMetricsAsDataFrame(self.spark, analysisResult)
        )
        
        analysisResult_df = (
            analysisResult_df
            .orderBy("entity", "instance", "name")
            .withColumn("dt_update", f.lit(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")))
        )

        return analysisResult_df

