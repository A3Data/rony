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

