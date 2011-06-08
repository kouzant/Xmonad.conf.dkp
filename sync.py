#!/usr/bin/env python

import shutil
import os

if __name__=="__main__":
    #Home Directory
    home=os.getenv("HOME")
    #Repository name
    repo=home+"/Xmonad.conf.dkp/"
    #Directories to copy
    #SOURCE:TARGET
    dirs={home+"/.xmonad/":".xmonad/",
            home+"/scripts/xmobar/":"scripts/xmobar/",
            home+"/scripts/xmonad/":"scripts/xmonad/"}
    #Files to copy    
    files=(home+"/.Xdefaults",
            home+"/.xmobarrc",
            home+"/.xsession")

    #First copy the directories
    for dir,name in dirs.items():
        repoDir=repo+name
        #shutli.copytree() needs the target directory
        #not to exist
        if os.path.exists(repoDir):
            shutil.rmtree(repoDir)
        shutil.copytree(dir,repoDir)

    #Copy the files
    for file in files:
        shutil.copy2(file,repo)
