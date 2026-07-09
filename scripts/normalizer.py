import os
import pandas as pd


class DataNormalizer:

    def __init__(self, dataframes, output_path="data/processed"):
        self.dataframes = dataframes
        self.output_path = output_path

        os.makedirs(self.output_path, exist_ok=True)

    def normalize(self):

        print("=" * 60)
        print("Data Normalization")
        print("=" * 60)

        cleaned_data = {}

        for file_name, df in self.dataframes.items():

            print(f"\nProcessing {file_name}")

            # Standardize column names
            df.columns = (
                df.columns
                .str.strip()
                .str.lower()
                .str.replace(" ", "_")
            )

            # Remove duplicate rows
            df = df.drop_duplicates()

            # Replace blank strings with NA
            df = df.replace("", pd.NA)

            cleaned_data[file_name] = df

            output_file = os.path.join(self.output_path, file_name)

            df.to_excel(output_file, index=False)

            print(f"Saved cleaned file -> {output_file}")

        return cleaned_data