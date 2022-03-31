import yaml
from pyspark.sql.dataframe import DataFrame
from .data_quality import DataQuality
from pyspark.sql import SparkSession, DataFrame
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
    Abstract DataQuality Class

    Parameters
    ----------
    spark: SparkSession
        A SparkSession object to run DataQuality jobs.
    """

    def __init__(self, spark: SparkSession) -> None:
        super().__init__(spark)


    def _analysis_job_builder(self, config_path: str) -> str:
        """
        WIP - For now, only works with single column methods.
        Build the Analyzer job code as a string expression to be evaluated.

        Parameters
        ----------
        config_path: str
            Path to a json config file.
            Config file should have column names as keys and lists of
            analysis methods as values.

            Example:
            {"PassengerId": ["Completeness"],
            "Age": ["Mean", "StandardDeviation", "Minimum", "Maximum"]}

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
            expression += ".addAnalyzer(" + method + '('
            for col in metricsconfig[method]:
                expression += '"' + col + '", '
            expression += '))'

        expression += ".run()"
        return expression


    def run(self, df: DataFrame, config: str) -> DataFrame:
        """
        Run the DataQuality job

        Parameters
        ----------

        df: DataFrame
            A Spark DataFrame to run DataQuality jobs.

        config: str
            Path to a json config file or a str expression of AnalysisRunner
            to evaluate

        Returns
        -------

        DataFrame -> A DataFrame with the results for DataQuality job.
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
        return analysisResult_df

