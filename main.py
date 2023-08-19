from utils.adb import ADB
from colorama import Fore as font
from questionary import text
from subprocess import run
from pathlib import Path
from time import sleep, perf_counter


def how_many():
    def only_int(inp):
        try:
            int(inp)
            return True
        except ValueError:
            return "僅可輸入數字"

    return int(text(
        "執行幾次",
        validate=only_int
    ).ask())


run("cls", shell=True, capture_output=True)
adb = ADB()
adb.connect()
count = how_many()

from utils.model import check_start

for i in range(count):
    print(f"已完成{font.YELLOW}{str(i)}{font.RESET}次")
    adb.tap(1100, 670)
    sleep(2)
    adb.tap(1100, 500)
    start = perf_counter()
    while True:
        sleep(3)
        adb.screenshot()
        stage, value = check_start()
        if stage == 1 or perf_counter() == start + 180:  # 結算
            sleep(2)
            adb.tap(1000, 500)
            sleep(5)
            break
print(f"{font.RED}已結束{font.RESET}")

