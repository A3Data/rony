from abc import ABC, abstractmethod
from pyspark.sql import SparkSession, DataFrame


class DataQuality(ABC):
    """
    Abstract DataQuality Class

    Parameters
    ----------
    spark: SparkSession
        A SparkSession object to run DataQuality jobs.
    """

    @abstractmethod
    def __init__(self, spark: SparkSession) -> None:
        self.spark = spark


    @abstractmethod
    def run(self, df: DataFrame) -> DataFrame:
        """
        Run the DataQuality process

        Parameters
        ----------

        df: DataFrame
            A Spark DataFrame to run DataQuality jobs.

        Returns
        -------

        DataFrame -> A DataFrame with the results for DataQuality job.
        """
        pass


    @abstractmethod
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
        pass
