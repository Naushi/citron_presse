import os
from typing import List, cast, Dict, Any

import pandas as pd
from constants import EXCEL_FILE, PDF_FOLDER
from check import check_folders
from load import load_data
from compute import compute_prints
from merge import merge_prints

# create file with all that
# finish

def main() -> None:
    raw_badges, fandoms, df = load_data()
    #check_folders(fandoms, df)
    badges = compute_prints(raw_badges)
    print(badges)
    merge_prints(badges)


if __name__ == "__main__":
    main()
