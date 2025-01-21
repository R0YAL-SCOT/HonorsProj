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
    parser.add_argument("-fO", metavar="file", required=True, help="Name of the output file for gvm")
    parser.add_argument("-fB", metavar="file", required=True, help="Name of the output file for Bloodhound")

    args = parser.parse_args()
    ipaddress = args.i
    nmapFileName = args.fN
    openvasFileName = args.fO
    bloodhoundFileName = args.fB

    if args.O:
        gvm(ipaddress, openvasFileName)
    
    if args.B:
        bloodhound(ipaddress, bloodhoundFileName)

    if args.N:
        nmap(ipaddress, nmapFileName)


def nmap(ipaddress, filename):
    #uses cve script and outputs results into a grepable file
    runNmap='nmap --script vuln --open -A -Pn -sT '+str(ipaddress)+' -oG '+chr(34)+filename+chr(34)

    #print(runNmap)
    exit_code = os.system(runNmap)
    exit_status = exit_code >> 8
    if exit_status:
        print("ERROR: Nmap failed to run")
    exit(1)

    print("Info: Output can be found in " + filename)



def gvm(ipaddress, filename):
    #need to have gvm scripts from github in the local directory or a full path to them
    
    #start the gvm system
    os.system('gvm start')

    #create task and start
    
    #use a script to run a certain script for vulnerability scan
    os.system('gvm-script --gmp-username name --gmp-password pass ssh --hostname <gsm> scripts/start-nvt-scan.gmp.py <oid of nvt> <target>')
    #requests pdf report of previous scan by report_id
    os.system('gvm-script --gmp-username name --gmp-password pass ssh --hostname <gsm> scripts/pdf-report.gmp.py <report_id> <pdf_file>')


def bloodhound(ipaddress, filename):
    
    #download bloodhound ce and run using os library
    #system needs to pip install or git clone bloodhound-ce before it can be used
    #the script could do it for the user but unsure
    print()
    
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