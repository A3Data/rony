from pyspark.sql.dataframe import DataFrame
from .data_quality import DataQuality
from pyspark.sql import SparkSession, DataFrame


class Profiler(DataQuality):
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
        pass


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

