import subprocess


class Decker:
    def __init__(self, build: bool = False, image_name: str = "myapp:latest") -> None:
        super().__init__("Decker")
        self.build = build
        self.image_name = image_name

    def build_image(self):
        try:
            subprocess.run(f"docker build -t {self.image_name} .", check=True)
        except subprocess.CalledProcessError as e:
            print(f"Docker imajı oluşturulurken hata: {e}")

    def GetDW(self):
        return self.build