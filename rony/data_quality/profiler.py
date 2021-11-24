from .data_quality import DataQuality
from pyspark.sql import DataFramen


class Profiler(DataQuality):
    """
    Abstract DataQuality Class

    Parameters
    ----------
    spark: SparkSession
        A SparkSession object to run DataQuality jobs.

    """

    def run(self, df: DataFrame) -> None:
        """
        Run the DataQuality process
        """
        pass


    def write_output(self, dataframe: bool = True) -> None:
        """
        Write output for DataQuality process.

        Parameters
        ----------

        dataframe: bool = True
            if True, results are returned as a spark DataFrame. If False,
            results are returned as a dict object.
        """
        if dataframe:
            pass
        else:
            pass

