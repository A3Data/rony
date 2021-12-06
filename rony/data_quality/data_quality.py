from abc import ABC, abstractmethod
from pyspark.sql import SparkSession, DataFrame


class DQ(ABC):
    """
    Abstract DataQuality Class

    Parameters
    ----------
    spark: SparkSession
        A SparkSession object to run DataQuality jobs.
        SparkSession must have two configurations:
        .config("spark.jars.packages", "com.amazon.deequ:deequ:2.0.0-spark-3.1")
        .config("spark.jars.excludes", "net.sourceforge.f2j:arpack_combined_all")
    """

    @abstractmethod
    def __init__(self, spark: SparkSession) -> None:
        if isinstance(spark, SparkSession):
            self.spark = spark
        else:
            raise TypeError("spark must be a valid SparkSession object.")


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


class DataQuality(DQ):
    """
    Base DataQuality Class

    Parameters
    ----------
    spark: SparkSession
        A SparkSession object to run DataQuality jobs.
        SparkSession must have two configurations:
        .config("spark.jars.packages", "com.amazon.deequ:deequ:2.0.0-spark-3.1")
        .config("spark.jars.excludes", "net.sourceforge.f2j:arpack_combined_all")
    """

    def __init__(self, spark: SparkSession) -> None:
        super().__init__(spark)


    @classmethod
    def create_pydeequ_SparkSession(cls) -> SparkSession:
        """
        Creates a default SparkSession with PyDeequ jars.
        """
        return (
            SparkSession
            .builder
            .config("spark.jars.packages", "com.amazon.deequ:deequ:2.0.0-spark-3.1")
            .config("spark.jars.excludes", "net.sourceforge.f2j:arpack_combined_all")
            .getOrCreate()
        )



    @classmethod
    def create_complete_SparkSession(cls) -> SparkSession:
        """
        Creates a SparkSession with PyDeequ and Delta jars
        and necessary configurations.
        """
        return (
            SparkSession
            .builder
            .config("spark.jars.packages", "com.amazon.deequ:deequ:2.0.0-spark-3.1,io.delta:delta-core_2.12:1.0.0")
            .config("spark.jars.excludes", "net.sourceforge.f2j:arpack_combined_all")
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
            .getOrCreate()
        )


    def write_output(self, df: DataFrame, path: str,
                     mode: str = "overwrite", delta: bool = True) -> None:
        """
        Write output for DataQuality process.

        Parameters
        ----------
        df: DataFrame
            The DataFrame object to write to an external object storage
        path: str
            The path to write the results. Usually, an S3/GCS/Blob Storage
            path
        mode: str
            Write mode for parquet or delta table. One of "overwrite",
            "append", "error" or "ignore". Defaults to "overwrite".
        delta: bool
            If True, write a delta table on specified path. If False, write a
            simple parquet file. Defaults to True.
        """
        if delta:
            output_format = "delta"
        else:
            output_format = "parquet"

        (
            df.write
            .mode(mode)
            .format(output_format)
            .save(path)
        )

