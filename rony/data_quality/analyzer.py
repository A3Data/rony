from pyspark.sql.dataframe import DataFrame
from .data_quality import DataQuality
from pyspark.sql import SparkSession, DataFrame
from pydeequ.analyzers import (
    AnalysisRunner, AnalyzerContext, Size, Completeness, Mean,
    Correlation, ApproxCountDistinct
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


    def run(self, df: DataFrame) -> DataFrame:
        """
        Run the DataQuality job

        Parameters
        ----------

        df: DataFrame
            A Spark DataFrame to run DataQuality jobs.

        Returns
        -------

        DataFrame -> A DataFrame with the results for DataQuality job.
        """
        analysisResult = (
            AnalysisRunner(self.spark)
                .onData(df)
                .addAnalyzer(Size())
                .addAnalyzer(Completeness("PassengerId"))
                .addAnalyzer(ApproxCountDistinct("Pclass"))
                .addAnalyzer(Mean("Age"))
                .addAnalyzer(Correlation("Age", "Fare"))
                .run()
        )

        analysisResult_df = (
            AnalyzerContext
                .successMetricsAsDataFrame(self.spark, analysisResult)
        )
        return analysisResult_df

