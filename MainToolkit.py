#Penetration testing toolkit
#Author: Andrew Walker

from getpass import getpass
import argparse
import os

def flags():

    #user input using params
    #Command line arguments creation and declaration
    parser = argparse.ArgumentParser(description="Python Penetration Testing Toolkit for Windows, Version: 1")

    parser.add_argument("-O", metavar="function", required=False, help="Use OpenVAS")
    parser.add_argument("-B", metavar="function", required=False, help="Use BloodHound")
    parser.add_argument("-N", metavar="function", required=False, help="Use Nmap")
    parser.add_argument("-i", metavar="target", required=True, help="IP address or address range to be tested")
    parser.add_argument("-fN", metavar="file", required=True, help="Name of the output file for Nmap")
    parser.add_argument("-fO", metavar="file", required=True, help="Name of the output file for OpenVAS")
    parser.add_argument("-fB", metavar="file", required=True, help="Name of the output file for Bloodhound")

    args = parser.parse_args()
    ipaddress = args.i
    nmapFileName = args.fN
    openvasFileName = args.fO
    bloodhoundFileName = args.fB

    if args.O:
        openVAS(ipaddress, openvasFileName)
    
    if args.B:
        bloodhound(ipaddress, bloodhoundFileName)

    if args.N:
        nmap(ipaddress, nmapFileName)


def nmap(ipaddress, filename):
    #using script vuln to get CVE codes, use codes to find auxillary scanners in Metasploit
    #speed, ip address and file type
    #might be too much information in nmap scan
    runNmap='nmap --script vuln --open -A -Pn -sT '+str(ipaddress)+' -oG '+chr(34)+filename+chr(34)

    print(runNmap)
    exit_code = os.system(runNmap)
    exit_status = exit_code >> 8
    if exit_status:
        print("ERROR: Nmap failed to run")
    exit(1)

    print("Info: Output can be found in " + filename)



def openVAS(ipaddress, filename):

    print("openVAS")
    #do something here

def bloodhound(ipaddress, filename):
    
    print("bloodhound")
    #do something here

'''
def metasploit():

    #start with finding nmap file and using reg ex to find CVE codes
    #launch msfconsole and do 'search cve:<CVE_code_here>'


    #start rpc server with standard username and password and set deamon to foreground
    runmsfrpcd='msfrpcd -U user -P password -a 127.0.0.1 -f'
    #connect to rpc server on localhost and use previous set username and password
    runmsfrpc='msfrpc -U user -P password -a 127.0.0.1'
    #run the auxillary PoC scanner using the input data from the user
    runMSF='rpc.call("module.execute", "auxillary", "put scanner here", {"put required data here, host, port, etc"})'
    
'''

if __name__=="__main__":
    flags()
    
    
    #nmap()
    #openVAS()
    #metasploit()