import pandas as pd

from constants import EXCEL_FILE
from typing import List, cast

def load_data():
    df = pd.read_excel(EXCEL_FILE)
    df = df[:-2]
    raw_badges = df.query('`Feuilles à imprimer` > 0')[['Fandom', 'Nom du Badge', 'Feuilles à imprimer']].to_dict('records')
    fandoms: List[str] = cast(List[str], df["Fandom"].unique())
    
    return raw_badges, fandoms, df
