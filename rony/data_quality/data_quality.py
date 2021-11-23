from abc import ABC, abstractmethod
from pyspark.sql import SparkSession


class DataQuality(ABC):
    """
    Abstract DataQuality Class
    """

    @abstractmethod
    def __init__(self, spark: SparkSession) -> None:
        self.spark = spark


    @abstractmethod
    def run(self) -> None:
        """
        Run the DataQuality process
        """
        pass


    @abstractmethod
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

