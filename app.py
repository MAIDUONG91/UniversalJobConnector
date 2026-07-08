from services.excel_reader import ExcelReader


def main():

    reader = ExcelReader()

    config = reader.load()

    print(config)


if __name__ == "__main__":

    main()