from . import Decker , Gethub

class GEHUB:
    def __init__(self, github: Gethub=None, docker: Decker=None) -> None: # type: ignore
        self.gh = github
        self.dk = docker

    def pushRepo(self):
        """Pushes the repo with Docker build check."""
        try:
            if not self.dk.GetDW():
                print("Git reposu başlatılıyor...")
                self.gh.run()
                print("işlemler bitti.")
            else:
                print("Docker görüntüsü oluşturuluyor...")
                self.dk.build_image()
                self.gh.run()
            print("Git işlemleri tamamlandı.")
        except Exception as e:
            print(f"GEHUB işlemi sırasında hata: {e}")

    @staticmethod
    def fcodef(name: str):
        """Generates a Python file with basic GitHub and Docker setup."""
        content = (
            "from modules import *\n\n"
            "name = ''\n"
            "projePath = r'C:\\example\\...' \n"
            "repoPath = 'https://github.com/userName/example.git'\n"
            "branchName = ''\n"
            "commitMessage = 'first commit'\n"
            "readmeText = ''\n\n"
            "git = Gethub(name, projePath, repoPath, branchName, commitMessage, ReMDMessage=readmeText)\n"
            "doc = Decker(False)\n"
            "ghub = GEHUB(git, doc)\n"
            "ghub.pushRepo()\n"
        )
        try:
            with open(f"{name}.py", 'w') as f:
                f.write(content)
            print(f"{name}.py dosyası başarıyla oluşturuldu.")
        except Exception as e:
            print(f"{name}.py dosyası oluşturulurken hata: {e}")