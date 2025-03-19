from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate data ingestion")
        data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        print(data_ingestion_artifacts)

        data_validation_config= DataValidationConfig(training_pipeline_config)
        data_validation= DataValidation(data_ingestion_artifacts, data_validation_config)
        logging.info("Initaite data validation")
        data_validation_artifact= data_validation.initiate_data_validation()
        logging.info("Data Validation completed")
        print(data_validation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)