import os
from src.logger import logging
from src.exception import CustomException
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class dataIngestionConfig:
    train_data_path = os.path.join("artifacts","train_data.csv")
    test_data_path = os.path.join("artifacts","test_data.csv")
    raw_data_path = os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=dataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebooks\data\StudentsPerformance.csv")
            logging.info("exported the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
            
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
            