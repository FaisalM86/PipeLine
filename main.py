import pandas as pd
from src.data_ingetion import load_data
from src.data_cleaning  import clean_data
from src.data_tranformation import transform_data
from src.data_output  import output_data

def main():
    """
    This function orchestrates the data pipeline.
    """
    try:
        # Define the file paths
        input_file_path = 'data.csv'
        output_file_path = 'transformed_data.csv'

        # Load the data
        data = load_data(input_file_path)

        # Clean the data
        cleaned_data = clean_data(data)

        # Transform the data
        transformed_data = transform_data(cleaned_data)

        # Output the data
        output_data(transformed_data, output_file_path)

        print("Data pipeline executed successfully.")
    except Exception as e:
        print("An error occurred while executing the data pipeline.")
        print(str(e))

if __name__ == "__main__":
    main()
