#Penetration testing toolkit
#Author: Andrew Walker
#my comment!

from getpass import getpass
import argparse
import os

def flags():

    '''
    #user input using params
    #Command line arguments creation and declaration
    parser = argparse.ArgumentParser(description="Python Penetration Testing Toolkit for Windows, Version: 1")

    parser.add_argument("-t", metavar="target", required=True,
                        help="Network Address range")
    parser.add_argument("-T", type=int, choices=[0, 1, 2, 3, 4, 5], required=True, 
                        help="Enter timing value for Nmap (0-5)")
    parser.add_argument("-n", metavar="filename", required=True,
                        help="Nmap ouput file name")
    
    #add and change next args
    parser.add_argument("-u", metavar="username", required=True,
                        help="Username for Nessus")
    #group creation so at least one password option is used but not both
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-P", metavar="password",
                        help="Password for Nessus")
    group.add_argument("-p", action="store_true", 
                        help="Interactively prompt for Nessus password")
    args = parser.parse_args()

    if args.p:
        password = getpass("Enter Nessus password: ")
    else:
        password = args.P

    ipaddress = args.t
    timing = args.T
    filename = args.n
    username = args.u


    '''


def nmap():
    #using script vuln to get CVE codes, use codes to find auxillary scanners in Metasploit
    #speed, ip address and file type
    #might be too much information in nmap scan
    runNmap='nmap --script vuln --open -A -Pn -sT -T'+str()+' '+str()+' -oX '+chr(34)++chr(34)
'''
    print(runNmap)
    exit_code = os.system(runNmap)
    exit_status = exit_code >> 8
    if exit_status:
        print("ERROR: Nmap failed to run")
    exit(1)

    print("Info: Output can be found in " + filename)
'''


def openVAS():

    runOpenVAS=''


def metasploit():

    #start with finding nmap file and using reg ex to find CVE codes
    #launch msfconsole and do 'search cve:<CVE_code_here>'


    #start rpc server with standard username and password and set deamon to foreground
    runmsfrpcd='msfrpcd -U user -P password -a 127.0.0.1 -f'
    #connect to rpc server on localhost and use previous set username and password
    runmsfrpc='msfrpc -U user -P password -a 127.0.0.1'
    #run the auxillary PoC scanner using the input data from the user
    runMSF='rpc.call("module.execute", "auxillary", "put scanner here", {"put required data here, host, port, etc"})'
    
    
if __name__=="__main__":
     nmap()
    #openVAS()
    #metasploit()