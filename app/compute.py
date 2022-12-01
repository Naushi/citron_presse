from typing import Dict, List


def compute_prints(raw_badges):
    badges: Dict[str, List] = {}
    for badge in raw_badges:
        if badge["Fandom"] not in badges:
            badges[badge["Fandom"]] = []
        badges[badge["Fandom"]].append(
            {"name": badge["Nom du Badge"], "qty": int(badge["Feuilles à imprimer"])}
        )
    return badges
