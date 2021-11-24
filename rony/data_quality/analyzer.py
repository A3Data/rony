from pyspark.sql.dataframe import DataFrame
from .data_quality import DataQuality
from pyspark.sql import DataFrame
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


    def write_output(self, df: DataFrame, path: str,
                     delta: bool = True) -> None:
        """
        Write output for DataQuality process.

        Parameters
        ----------
        df: DataFrame
            The DataFrame object to write to an external object storage
        path: str
            The path to write the results. Usually, an S3/GCS/Blob Storage
            path
        delta: bool
            If True, write a delta table on specified path. If False, write a
            simple parquet file.
        """
        if delta:
            output_format = "delta"
        else:
            output_format = "parquet"

        (
            df.write
            .format(output_format)
            .save(path)
        )

