import os
import requests as requests

cookie = os.environ.get("AOC_COOKIE")


def get_input(day: int, year: int = 2024) -> str:
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": cookie}
    )
    return res.text.strip()
