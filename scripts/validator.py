import pandas as pd


class DataValidator:
    def __init__(self, dataframes):
        self.dataframes = dataframes

    def validate(self):
        print("=" * 60)
        print("Data Validation Report")
        print("=" * 60)

        for file_name, df in self.dataframes.items():

            print(f"\nFile: {file_name}")

            print(f"Rows: {df.shape[0]}")
            print(f"Columns: {df.shape[1]}")

            missing = df.isnull().sum().sum()
            print(f"Missing Values: {missing}")

            duplicates = df.duplicated().sum()
            print(f"Duplicate Rows: {duplicates}")

            print("\nColumn Data Types:")
            print(df.dtypes)