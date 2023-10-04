
import pandas as pd

def output_data(data, file_path):
    """
    This function outputs the data to a csv file.
    :param data: DataFrame, The data to be output.
    :param file_path: str, The path of the output file.
    """
    try:
        # Write the DataFrame to csv
        data.to_csv(file_path, index=False)
        print("Data outputted successfully.")
    except Exception as e:
        print("An error occurred while outputting the data.")
        print(str(e))

if __name__ == "__main__":
    from src.data_ingetion  import load_data
    from src.data_cleaning  import clean_data
    from src.data_tranformation import transform_data

    input_file_path = '../data/raw_data.csv'
    output_file_path = '../data/transformed_data.csv'

    data = load_data(input_file_path)
    cleaned_data = clean_data(data)
    transformed_data = transform_data(cleaned_data)
    output_data(transformed_data, output_file_path)
