#!/usr/bin/python3.6

import sys
import subprocess
import os


for a in list(range(20,41)) + list(range(46,60)) + list(range(67,70)) + list(range(75,102)):
                cmd = "ps aux | grep haproxy | grep -v grep | awk '{print $13}' | awk -F/ '{print $4}' | awk -F. '{print $1}'"
                out, err = subprocess.Popen("ssh alok@serv"+ str(a) +"i /usr/bin/sudo " + cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()
                out =  out[:-1].decode('utf-8').split("\n")
                for i in out:
                                if i == "haproxy-main-sendproxy":
                                                i = "haproxy-main"
                                                r = "/var/run/" + i +".sock"
                                                cmd1 = "\"echo 'show stat' | sudo nc -U " + r + "| cut -d ',' -f 2,19,18,37,20,21,3,4,5,6 | column -s, -t\""
                                                out1, err1 = subprocess.Popen("ssh alok@serv" + str(a) + "i " + cmd1 + " > /home/alok/alok_scripts/serv" + str(a) + "i_" + i  + ".txt" , shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()
                                elif i  == "":
                                                print("No HaProxy Running on Server")
                                else:
                                                r = "/var/run/" + i +".sock"
                                                cmd1 = "\"echo 'show stat' | sudo nc -U " + r + "| cut -d ',' -f 2,19,18,37,20,21,3,4,5,6 | column -s, -t\""
                                                out1, err1 = subprocess.Popen("ssh alok@serv" + str(a) + "i " + cmd1 + " > /home/alok/alok_scripts/serv" + str(a) + "i_" + i  + ".txt" , shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()
