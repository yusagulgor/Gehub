from modules import *

name = '' 
projePath = 'C:\example\...' 
repoPath = 'https://github.com/userName/example.git' 
branchName = '' 
commitMessage = 'first commit' 
readmeText = '' 

git = Gethub(name,projePath,repoPath,branchName,commitMessage,ReMDMessage=readmeText)
doc = Decker(False)
ghub = GEHUB(git,doc)
ghub.pushRepo()
