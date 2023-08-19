from subprocess import run
from questionary import select


def shell(command):
    return run(command, shell=True, capture_output=True)


class ADB:
    def __init__(self):
        self.device: str = ""
        result = shell("adb devices")
        try:
            self.devices = [i.split("\t")[0] for i in result.stdout.decode("utf8").split("\r\n")[1:] if not i == ""]
        except IndexError:
            self.err = "has not any device"
            self.error()

    def error(self):
        return self.err

    def connect(self):
        self.device = select(
            "choose the device",
            choices=self.devices
        ).ask()

    def tap(self, x, y):
        shell(f"adb -s {self.device} shell input tap {x} {y}")

    def screenshot(self):
        img_path = fr".\data\img\img.png"
        shell(fr"adb -s {self.device} exec-out screencap -p > {img_path}")
        return img_path
