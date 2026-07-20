import sqlite3
import pandas as pd
import os


class DatabaseLoader:

    def __init__(self,
                 processed_path="data/processed",
                 database="db/n100.db"):

        self.processed_path = processed_path
        self.database = database

    def load_to_database(self):

        conn = sqlite3.connect(self.database)

        print("=" * 60)
        print("Loading Data into SQLite")
        print("=" * 60)

        for file in os.listdir(self.processed_path):

            if file.endswith(".xlsx"):

                table_name = file.replace(".xlsx", "")
                file_path = os.path.join(self.processed_path, file)

                if table_name == "companies":
                    df = pd.read_excel(file_path, header=1)
                else:
                    df = pd.read_excel(file_path)

                df.to_sql(
                    table_name,
                    conn,
                    if_exists="replace",
                    index=False
                )

                print(f"{table_name} loaded successfully.")

        conn.close()

        print("\nDatabase loading completed.")


if __name__ == "__main__":
    loader = DatabaseLoader()
    loader.load_to_database()