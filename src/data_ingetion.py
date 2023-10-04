
import pandas as pd

def load_data(file_path):
    """
    This function loads the data from the given file path.
    :param file_path: str, The path of the file to be loaded.
    :return: DataFrame, The loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print("An error occurred while loading the data.")
        print(str(e))

if __name__ == "__main__":
    file_path = '../data.csv'
    data = load_data(file_path)
    print(data.head())
