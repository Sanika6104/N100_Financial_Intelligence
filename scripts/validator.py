import os
import pandas as pd


class DataValidator:

    def __init__(self, dataframes, output_folder="output"):
        self.dataframes = dataframes
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def validate(self):

        report = []

        print("="*60)
        print("Validation Report")
        print("="*60)

        for file_name, df in self.dataframes.items():

            missing = df.isnull().sum().sum()
            duplicates = df.duplicated().sum()

            report.append({
                "File": file_name,
                "Rows": len(df),
                "Columns": len(df.columns),
                "Missing Values": missing,
                "Duplicate Rows": duplicates
            })

            print(f"{file_name} ✔")

        report_df = pd.DataFrame(report)

        report_df.to_csv(
            os.path.join(self.output_folder,"validation_report.csv"),
            index=False
        )

        print("\nValidation report saved.")