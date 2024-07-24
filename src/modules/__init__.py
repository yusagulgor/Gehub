from modules.dm import Decker
from modules.gm import Gethub

class GEHUB:
    def __init__(self, github: Gethub, docker: Decker) -> None:
        self.gh = github
        self.dk = docker

    def pushRepo(self):
        if not self.dk.GetDW():
            self.gh.initialize_git_repo()
        else:
            try:
                self.dk.build_image()    
                self.gh.initialize_git_repo()
            except Exception as e:
                print(e)    
            else:    
                print("Git işlemleri tamamlandı.")


def fcodef(name: str):
    with open(name+".py", 'w') as f:
        f.write("from modules import *\n\n")
        f.write("name = '' \n")
        f.write("projePath = 'C:\\example\\...' \n")
        f.write("repoPath = 'https://github.com/userName/example.git' \n")
        f.write("branchName = '' \n")
        f.write("commitMessage = 'first commit' \n")
        f.write("readmeText = '' \n\n")

        f.write("git = Github(name,projePath,repoPath,branchName,commitMessage,ReMDMessage=readmeText)\n")
        f.write("doc = Docker(False)\n")
        f.write("ghub = GEHUB(git,doc)\n")
        f.write("ghub.pushRepo()\n")


__all__ = ["GEHUB", "Gethub", "Decker","fcodef"]
