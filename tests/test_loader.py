from scripts.loader import DataLoader


def test_loader():

    loader = DataLoader()

    data = loader.load_excel_files()

    assert len(data) > 0