import os
from typing import Any, Dict, List, cast

import pandas as pd

from check import check_folders
from compute import compute_prints
from constants import EXCEL_FILE, PDF_FOLDER
from load import load_data
from merge import merge_prints


def main() -> None:
    raw_badges, fandoms, df = load_data()
    check_folders(fandoms, df)
    badges = compute_prints(raw_badges)
    print(badges)
    merge_prints(badges)


if __name__ == "__main__":
    main()
