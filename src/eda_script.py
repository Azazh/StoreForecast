import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import logging


# Initialize Logging
def init_logging():
    logging.basicConfig(
        filename='notebooks/eda_log.log',  # Ensure correct path
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()


logger = init_logging()


# Load Datasets
def load_data():
    try:
        train = pd.read_csv('data/rossmann_store_sales/train.csv')
        test = pd.read_csv('data/rossmann_store_sales/test.csv')
        store = pd.read_csv('data/rossmann_store_sales/store.csv')
        logger.info("Datasets loaded successfully.")
        return train, test, store
    except Exception as e:
        logger.error(f"Error loading datasets: {e}")
        raise


# Merge Datasets
def merge_data(train, test, store):
    try:
        train = train.merge(store, on='Store', how='left')
        test = test.merge(store, on='Store', how='left')
        logger.info("Train and test datasets merged with store dataset.")
        return train, test
    except Exception as e:
        logger.error(f"Error merging datasets: {e}")
        raise


# Handle Missing Values
def handle_missing_values(train):
    try:
        imputer = SimpleImputer(strategy='mean')
        train['CompetitionDistance'] = imputer.fit_transform(train[['CompetitionDistance']])
        logger.info("Missing values handled for CompetitionDistance.")
    except Exception as e:
        logger.error(f"Error handling missing values: {e}")
        raise
