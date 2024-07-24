import os

class Decker:

    def __init__(self, build: bool = False,image_name: str = "myapp:latest") -> None:
        self.build = build
        self.image_name = image_name

    def build_image(self):
            os.system(f"docker build -t {self.image_name} .")

    def GetDW(self):
        return self.build

__all__ = ["Decker"]