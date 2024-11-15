#Penetration testing toolkit
#Author: Andrew Walker
#my comment!

from getpass import getpass
import argparse
import os

def main():


    nmap()
    metasploit()

    


def nmap():
    runNmap='nmap --open -A -Pn -sT -T'+str()+' '+str()+' -oX '+chr(34)++chr(34)

    print(runNmap)
    exit_code = os.system(runNmap)
    exit_status = exit_code >> 8
    if exit_status:
        print("ERROR: Nmap failed to run")
    exit(1)

    print("Info: Output can be found in " + filename)


def metasploit():
    #start rpc server with standard username and password and set deamon to foreground
    runmsfrpcd='msfrpcd -U user -P password -a 127.0.0.1 -f'
    #connect to rpc server on localhost and use previous set username and password
    runmsfrpc='msfrpc -U user -P password -a 127.0.0.1'
    #run the auxillary PoC scanner using the input data from the user
    runMSF='rpc.call("module.execute", "auxillary", "put scanner here", {"put required data here, host, port, etc"})'
