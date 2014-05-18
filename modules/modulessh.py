#!/usr/bin/python3.1

# This plugin is the SSH module

import modulessh
import sys
import subprocess
import os
import re
import shlex
import time
from subprocess import Popen, PIPE

# SSH function
def ssh():
    print("1. This module will teach you how to use ssh, on both side, server and client.\n")
    packagename = input("2. First, let's verify if ssh is install. Can you tell me what is the name of the package ssh server on Debian ?\n\n")
    while packagename != "openssh-server":
        packagename = input("No, this isn't the exact name. Please retry !\n\n")
    else:
        print("Nice ! You found it ! But that was easy ;D ")
        checkit = input("3. Now let's intall the package, start him and type 'check it' when you want.\n\n")
        while checkit != "check it":
            checkit = input("Type 'check it' to verify.\n")
        else:
            checkinstalledpackage = "dpkg -l openssh-server"
            process = subprocess.Popen(shlex.split(checkinstalledpackage), stdout=subprocess.PIPE)
            process.communicate()
            exit_code = process.wait()
            while exit_code != 0:
                time.sleep(1)
                retry = input("Openssh-server is not installed, please type 'check it' again.\n\n")
                checkinstalledpackage = "dpkg -l openssh-server"
                process = subprocess.Popen(shlex.split(checkinstalledpackage), stdout=subprocess.PIPE)
                process.communicate()
                exit_code = process.wait()
            else:
                checkit = input("4. Good ! Let's check if it's running now: type 'check it' to verify !\n\n")
                while checkit != "check it":
                    checkit = input("Type 'check it' to verify.\n")
                else:
                    checkdaemonrunning1 = "ps aux"
                    checkdaemonrunning2 = "grep sbin/sshd"
                    checkdaemonrunning3 = "grep -v grep"
                    process1 = subprocess.Popen(shlex.split(checkdaemonrunning1), stdout=subprocess.PIPE)
                    process2 = subprocess.Popen(shlex.split(checkdaemonrunning2), stdin=process1.stdout, stdout=subprocess.PIPE)
                    process1.stdout.close()
                    process3 = subprocess.Popen(shlex.split(checkdaemonrunning3), stdin=process2.stdout, stdout=subprocess.PIPE)
                    process2.stdout.close()
                    process3.communicate()
                    exit_code = process3.wait()
                while exit_code != 0:
                    time.sleep(1)
                    retry = input("5. Please, start the daemon ssh ! Type 'check it' to recheck.")
                    checkdaemonrunning1 = "ps aux"
                    checkdaemonrunning2 = "grep sbin/sshd"
                    checkdaemonrunning3 = "grep -v grep"
                    process1 = subprocess.Popen(shlex.split(checkdaemonrunning1), stdout=subprocess.PIPE)
                    process2 = subprocess.Popen(shlex.split(checkdaemonrunning2), stdin=process1.stdout, stdout=subprocess.PIPE)
                    process1.stdout.close()
                    process3 = subprocess.Popen(shlex.split(checkdaemonrunning3), stdin=process2.stdout, stdout=subprocess.PIPE)
                    process2.stdout.close()
                    process3.communicate()
                    exit_code = process3.wait()
                else:
                    print("Good ! Let's continue !\n\n")
                    print("This is the syntax of the ssh command : 'ssh <user>@<host> [-p <port>]'\n\n")
                    print("6. If you're ready, let's initialize the connection to the host 'localhost' with user 'root'.\n")
                    checkit = input("When you're connected, please, create an empty file in '/var/tmp/' with name 'mytest.txt' and type 'check it' when it's ok !\n")
                    while checkit != "check it":
                        checkit = input("Please, type 'check it'\n")
                    else:
                        while not os.path.exists("/var/tmp/mytest.txt"):
                            time.sleep(1)
                            retry = input("Please, create the file !\n")
                        else:
                            print("Good one !")
