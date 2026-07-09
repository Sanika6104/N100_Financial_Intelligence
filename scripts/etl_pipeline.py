from loader import DataLoader
from validator import DataValidator


def main():

    loader = DataLoader()
    dataframes = loader.load_excel_files()

    validator = DataValidator(dataframes)
    validator.validate()


if __name__ == "__main__":
    main()