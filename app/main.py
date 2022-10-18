import os
from typing import List, cast

import pandas as pd
from constants import EXCEL_FILE, PDF_FOLDER

# compute files needing to be printed
# create file with all that
# finish


def main() -> None:
    df = pd.read_excel(EXCEL_FILE)
    df = df[:-2]
    # print(df.query('`Feuilles à imprimer` > 0'))
    fandoms: List[str] = cast(List[str], df["Fandom"].unique())
    check_folders(fandoms, df)


def check_folders(fandoms: List[str], dataframe: pd.DataFrame) -> None:
    for value in fandoms:
        if os.path.exists(f"{PDF_FOLDER}{value}/"):
            check_files(value, dataframe)
        else:
            print(f"{value} is missing.")


def check_files(fandom: str, dataframe: pd.DataFrame) -> None:
    files = dataframe.query(f'`Fandom` == "{fandom}"')["Nom du Badge"].unique()
    for file in files:
        file_path = f"{PDF_FOLDER}{fandom}/{file}.pdf"
        if os.path.exists(file_path):
            pass
        else:
            print(f"{file_path} is missing.")


if __name__ == "__main__":
    main()
