import os

class Gethub:
    
    """
    # Usage
    pls click to class and read the doc

    pPath must be like this , "x:\\examples\\..." The important thing here is to double
    rPath: GitHub repository URL'si
    your_branchName: Git dalı adı
    commitMessage: İlk commit mesajı
    dwReMD: README.md dosyasının oluşturulup oluşturulmayacağını belirler
    ReMDMessage: README.md içeriği
    
    """

    def __init__(self, pName: str, pPath: str, rPath: str, your_branchName: str, commitMessage: str, dwReMD: bool = False, ReMDMessage: str = None) -> None:
        self.pName = pName
        self.pPath = pPath
        self.rPath = rPath
        self.y_bN = your_branchName
        self.cm = commitMessage
        self.dwMD = dwReMD
        self.mdMessage = ReMDMessage

        if self.dwMD and self.mdMessage is None:
            self.mdMessage = f"""
# {self.pName} project

hello to my {self.pName}

"""
        elif not self.dwMD and self.mdMessage is not None:
            self.mdMessage = None
        else:
            print("always okey")

    def GetpName(self): return self.pName
    def GetpPath(self): return self.pPath
    def GetrPath(self): return self.rPath
    def GetybName(self): return self.y_bN
    def GetCM(self): return self.cm
    def GetDWMD(self): return self.dwMD
    def GetMDmessage(self): return self.mdMessage

    def addRM(self):
        if self.dwMD and self.mdMessage:
            with open(os.path.join(self.pPath, 'README.md'), 'w') as f:
                f.write(self.mdMessage)

    def initialize_git_repo(self):
        if not os.path.exists(self.pPath):
            os.makedirs(self.pPath, exist_ok=True)
        
        os.system(f"git init {self.pPath}")
        self.addRM()
        os.system(f"git -C {self.pPath} add .")
        os.system(f'git -C {self.pPath} commit -m "{self.cm}"')
        os.system(f"git -C {self.pPath} branch -M {self.y_bN}")
        os.system(f"git -C {self.pPath} remote add origin {self.rPath}")
        os.system(f"git -C {self.pPath} push -u origin {self.y_bN}")

__all__ = ["Gethub"]

