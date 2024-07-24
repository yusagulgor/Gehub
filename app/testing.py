from modules import *

name = '' 
projePath = 'C:\example\...' 
repoPath = 'https://github.com/userName/example.git' 
branchName = '' 
commitMessage = 'first commit' 
readmeText = '' 

git = Github(name,projePath,repoPath,branchName,commitMessage,ReMDMessage=readmeText)
doc = Docker(False)
ghub = GEHUB(git,doc)
ghub.pushRepo()
