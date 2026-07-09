from loader import DataLoader
from validator import DataValidator
from normalizer import DataNormalizer
from db_loader import DatabaseLoader


def main():

    loader = DataLoader()
    dataframes = loader.load_excel_files()

    validator = DataValidator(dataframes)
    validator.validate()

    normalizer = DataNormalizer(dataframes)
    normalizer.normalize()

    database = DatabaseLoader()
    database.load_to_database()


if __name__ == "__main__":
    main()