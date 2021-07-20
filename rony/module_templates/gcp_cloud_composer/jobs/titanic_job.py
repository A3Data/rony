from google.cloud import logging
from pyspark.sql import SparkSession

DATALAKE_PATH = "gs://datalake_rony/"
FILE = "landing_zone/titanic.csv"

if __name__ == '__main__':
    # Log client instance
    logging_client = logging.Client()
    # Set up logger bound to the current client
    logger = logging_client.logger('pyspark_logger')
    # Create spark session
    spark = SparkSession.builder.appName('Titanic Job').getOrCreate()
    # Load csv file from datalake
    titanic = spark.read.format("csv")\
        .option("inferSchema", True)\
        .option("delimiter", ";")\
        .option("header", True)\
        .load(DATALAKE_PATH + FILE)

    # Core fields, which will be stored in the processing zone
    passengers = titanic.select("Name", "Sex", "Age").dropDuplicates()

    tickets = titanic.select("Ticket", "Pclass").dropDuplicates()

    try:
        # Save the file in the processing zone with parquet format
        passengers.write.format("parquet").save(DATALAKE_PATH + "processing_zone/passengers.parquet")

        tickets.write.format("parquet").save(DATALAKE_PATH + "processing_zone/tickets.parquet")
        # Successfully Log info
        logger.log_text("Passengers and Tickets loaded successfully", severity="INFO")
    except Exception as err:
        logger.log_text("Error to load Passengers and Tickets!", severity="ERROR")
