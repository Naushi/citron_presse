import os
from typing import List

import pandas as pd

from constants import PDF_FOLDER


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
        if not os.path.exists(file_path):
            print(f"{file_path} is missing.")
