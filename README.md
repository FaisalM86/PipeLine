# Data Engineering Pipeline

This project is a demonstration of a data engineering pipeline. It is designed to showcase the skills of a data scientist in handling, cleaning, transforming, and outputting data.

## Project Structure

The project has the following structure:

```
.
├── README.md
├── requirements.txt
├── data.csv
│   
├── src
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── data_transformation.py
│   ├── data_output.py
├── main.py
└── .gitignore
```

## Files Description

- `README.md`: This file, containing project description and instructions.
- `requirements.txt`: Contains the necessary libraries needed to run the project.
- `data.csv`: The raw data file that will be processed by the pipeline.
- `src/data_ingestion.py`: This script is responsible for ingesting the data from `raw_data.csv`.
- `src/data_cleaning.py`: This script is responsible for cleaning the ingested data.
- `src/data_transformation.py`: This script is responsible for transforming the cleaned data.
- `src/data_output.py`: This script is responsible for outputting the transformed data.
- `main.py`: This is the main script that runs the entire pipeline.
- `.gitignore`: This file specifies the untracked files that Git should ignore.

## How to Run

1. Clone this repository.
2. Install the necessary libraries listed in `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

3. Run the main script:

```bash
python src/main.py
```

This will run the entire data pipeline, from data ingestion to data output.

## Author

Faisal Mehmood

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
