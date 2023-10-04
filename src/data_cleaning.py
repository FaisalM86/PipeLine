import pandas as pd

def clean_data(data):
    """
    This function cleans the data.
    :param data: DataFrame, The data to be cleaned.
    :return: DataFrame, The cleaned data.
    """
    try:
        # Strip whitespace from columns
        data.columns = data.columns.str.strip()

        # Strip whitespace from string column's values
        for col in data.columns:
            if data[col].dtype == 'object':
                data[col] = data[col].str.strip()

        # Remove any rows with missing data
        data = data.dropna()

        # Convert age and salary to integers
        data['age'] = data['age'].astype(int)
        data['salary'] = data['salary'].astype(int)

        # Remove any rows where age is less than 18 or greater than 100
        data = data[(data['age'] >= 18) & (data['age'] <= 100)]

        # Remove any rows where salary is less than 0
        data = data[data['salary'] >= 0]

        print("Data cleaned successfully.")
        return data
    except Exception as e:
        print("An error occurred while cleaning the data.")
        print(str(e))

if __name__ == "__main__":
    from src.data_ingetion import load_data

    file_path = '../data.csv'
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    print(cleaned_data.head())