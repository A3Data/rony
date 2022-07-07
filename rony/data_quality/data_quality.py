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
        .config("spark.jars.packages", "com.amazon.deequ:deequ:2.0.1-spark-3.2")
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
        .config("spark.jars.packages", "com.amazon.deequ:deequ:2.0.1-spark-3.2")
        .config("spark.jars.excludes", "net.sourceforge.f2j:arpack_combined_all")
    """

    def __init__(self, spark: SparkSession) -> None:
        super().__init__(spark)


    @classmethod
    def create_pydeequ_SparkSession(cls, deequ_maven_package="com.amazon.deequ:deequ:2.0.1-spark-3.2") -> SparkSession:
        """
        Creates a default SparkSession with PyDeequ jars. 
        
        Parameters
        ----------

        deequ_maven_package: str
            Maven package to use in Spark application. Defaults to "com.amazon.deequ:deequ:2.0.1-spark-3.2".
        """
        return (
            SparkSession
            .builder
            .config("spark.jars.packages", deequ_maven_package)
            .config("spark.jars.excludes", "net.sourceforge.f2j:arpack_combined_all")
            .getOrCreate()
        )



    @classmethod
    def create_deequ_delta_SparkSession(cls, 
        deequ_maven_package="com.amazon.deequ:deequ:2.0.1-spark-3.2",
        delta_maven_package="io.delta:delta-core_2.12:1.2.1") -> SparkSession:
        """
        Creates a SparkSession with PyDeequ and Delta jars
        and necessary configurations.


        Parameters
        ----------

        deequ_maven_package: str
            Deequ maven package to use in Spark application. Defaults to "com.amazon.deequ:deequ:2.0.1-spark-3.2".

        delta_maven_package: str
            Delta maven package to use in Spark application. Defaults to "io.delta:delta-core_2.12:1.2.1"
        """
        return (
            SparkSession
            .builder
            .config("spark.jars.packages", f"{deequ_maven_package},{delta_maven_package}")
            .config("spark.jars.excludes", "net.sourceforge.f2j:arpack_combined_all")
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
            .getOrCreate()
        )


    def write_output(self, df: DataFrame, path: str,
                     mode: str = "append", delta: bool = True) -> None:
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
            "append", "error" or "ignore". Defaults to "append".
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

