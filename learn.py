#!/usr/bin/python3.1

# This plugin let you learn tool
##################################################

import sys
sys.path.append("modules/")
import modulessh
import subprocess
import os
import re
import shlex
import time
from subprocess import Popen, PIPE

def readytogo():
    answer = input("You're going to learn " + tool.upper() + ", are you ready to begin ? (yes/no)\n")

    if answer in ["N", "n", "No", "NO", "no"]:
        print("No problem, bye !")
    elif answer in ["Y", "y", "Yes", "YES", "yes"]:
        ready = input("Ok, nice ! So you have to open another terminal. Please type 'ready' when you are.\n\n")
        while ready != "ready":
            ready = input("Please type 'ready' when you're ready !\n\n")
    else:
        print("I didn't understood your answer, please type 'yes' or 'no'.\n\n")

                        
#####
#   #
# 1 #
#   #
#####

if len(sys.argv) != 2:
    print("Please, respect the syntax of the script !")
    print("Syntax : ./learn.py <tool>")
else:
    tool = sys.argv[1]
    if tool == "ssh":
        readytogo()
        modulessh.ssh()
    else:
        print("This tool, doesn't exist (yet). Please choose another one.")
        sys.exit(1)
