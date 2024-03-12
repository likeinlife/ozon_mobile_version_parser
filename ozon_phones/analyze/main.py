"""
Результат для файла items.jsonl.

Result
------
     os_version  count
3  Android 13.x     58
2    Android 13     44
4    Android 14     28
1  Android 12.x      6
0  Android 10.x      4
6   Android 9.x      2
5   Android 8.x      1
7        iOS 13      1
"""

from pathlib import Path

import pandas as pd


def main(file_path: Path):
    data = pd.read_json(file_path, lines=True)
    data["name"] = data["name"].str.replace("\n", "").str.strip(" ")
    print(
        data.groupby("os_version")["os_version"].count().reset_index(name="count").sort_values("count", ascending=False)
    )


if __name__ == "__main__":
    main(Path("items.jsonl"))
