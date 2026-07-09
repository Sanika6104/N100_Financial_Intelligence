from loader import DataLoader
from validator import DataValidator
from normalizer import DataNormalizer


def main():

    loader = DataLoader()
    dataframes = loader.load_excel_files()

    validator = DataValidator(dataframes)
    validator.validate()

    normalizer = DataNormalizer(dataframes)
    normalizer.normalize()


if __name__ == "__main__":
    main()