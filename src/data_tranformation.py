
import pandas as pd
import numpy as np


def transform_data(data):
    """
    This function transforms the data.
    :param data: DataFrame, The data to be transformed.
    :return: DataFrame, The transformed data.
    """
    try:
        # Create a new column 'income_category' based on 'salary'
        conditions = [
            (data['salary'] < 50000),
            (data['salary'] >= 50000) & (data['salary'] < 80000),
            (data['salary'] >= 80000)
        ]
        choices = ['Low', 'Medium', 'High']
        data['income_category'] = np.select(conditions, choices, default='Not Specified')

        # Create a new column 'age_group' based on 'age'
        conditions = [
            (data['age'] < 30),
            (data['age'] >= 30) & (data['age'] < 50),
            (data['age'] >= 50)
        ]
        choices = ['Young', 'Middle-aged', 'Senior']
        data['age_group'] = np.select(conditions, choices, default='Not Specified')

        print("Data transformed successfully.")
        return data
    except Exception as e:
        print("An error occurred while transforming the data.")
        print(str(e))

if __name__ == "__main__":
    from src.data_ingetion  import load_data
    from src.data_cleaning  import clean_data

    file_path = '../data.csv'
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    transformed_data = transform_data(cleaned_data)
    print(transformed_data.head())
