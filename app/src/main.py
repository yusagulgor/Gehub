from modules import *

pPath = ""
rPath = ""
bName = "main"
commitMessage = "ilk komit"

readmeText = """ """


git = Gethub("hi", pPath, rPath, bName, commitMessage, dwReMD=False)
doc = Decker(build=False)
ghub = GEHUB(git, doc)

ghub.pushRepo()
