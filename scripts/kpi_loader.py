import sqlite3
import pandas as pd


class KPILoader:

    def __init__(self, db_path="db/n100.db"):
        self.db_path = db_path

    def load_ratios(self):
        conn = sqlite3.connect(self.db_path)

        try:
            financial_ratios = pd.read_sql(
                "SELECT * FROM financial_ratios",
                conn
            )

            print("Financial Ratios Table")
            print(financial_ratios.head())

        except Exception as e:
            print("Error:", e)

        finally:
            conn.close()


if __name__ == "__main__":
    loader = KPILoader()
    loader.load_ratios()