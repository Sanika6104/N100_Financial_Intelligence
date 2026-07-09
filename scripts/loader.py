import os
import pandas as pd


class DataLoader:
    def __init__(self, data_path="data/raw"):
        self.data_path = data_path
        self.dataframes = {}

    def load_excel_files(self):
        print("=" * 60)
        print("Loading Excel Files")
        print("=" * 60)

        for file in os.listdir(self.data_path):
            if file.endswith(".xlsx"):
                file_path = os.path.join(self.data_path, file)

                try:
                    df = pd.read_excel(file_path)

                    self.dataframes[file] = df

                    print(f"\nFile: {file}")
                    print(f"Rows: {df.shape[0]}")
                    print(f"Columns: {df.shape[1]}")
                    print(f"Missing Values: {df.isnull().sum().sum()}")

                except Exception as e:
                    print(f"Error loading {file}: {e}")

        return self.dataframes


if __name__ == "__main__":
    loader = DataLoader()
    loader.load_excel_files()