#Penetration testing toolkit
#Author: Andrew Walker

#from gvmConnectionScript import connection
from getpass import getpass
#from regexReport import makeEnumReport
import argparse
import os
import subprocess


def nmap(ipaddress, filename):
    #uses cve script and outputs results into a grepable file
    try:
        scanNmap = subprocess.Popen(["nmap", "--script", "vuln", "--open", "-A", "-Pn", "-O", "-sV", "-sT", str(ipaddress),"-oX", str(filename)], stdout=subprocess.PIPE).stdout.read()
        print(scanNmap)
    
    except subprocess.CalledProcessError as err:
        print("Nmap has failed with return code:  {err.returncode}")


def lynis(ipaddress):
    #set for a remote host using IP address but could be used for local host but the nature of this toolkit means this wouldn't happen.
    #Using the pentest option with no output and no log file to reduce the amount of unneeded information
    try:
        lynis = subprocess.Popen(["lynis", "audit system remote", str(ipaddress), "--pentest", "--quiet", "--no-log" ], stdout=subprocess.PIPE).stdout.read()
        print(lynis)
    
    except subprocess.CalledProcessError as err:
        print("Lynis has failed with return code:  {err.returncode}")


def bloodhound(ipaddress, username, password, domain):
    
    #download bloodhound ce and run using os library
    #system needs to pip install or git clone bloodhound-ce before it can be used

    #collect all information on domain
    #username and password must be known before running this command
    try:
        bH = subprocess.Popen(["bloodhound-python", "-u", str(username), "-p", str(password), "-d", str(domain), "-ns", str(ipaddress), "-c", "All"], stdout=subprocess.PIPE).stdout.read()
        print(bH)

    except subprocess.CalledProcessError as err:
        print("Bloodhound-python has failed with return code:  {err.returncode}")

    #output gives json files in working directory
    #regex file will need to find and grab all json files

'''
def gvm(username, password, ipaddress, filename):
    #need to have gvm scripts from github in the local directory or a full path to them
    #run 'python3 -m pip install --user python-gvm' to use the gvm python library
    #https://github.com/greenbone/python-gvm
    #https://www.youtube.com/watch?v=J7SrS4qDzM0&t=95s - tutorial
    #start the gvm system
    #use threads for different tasks
    os.system('gvm start')

    #connection(username, password)
    #create task and start
    #no target ID so it creates one
    os.system('gvm-cli ssh --gmp-username '+str(username)+' --gmp-password '+str(password)+' --xml "<create_task><name>vuln scan</name>><scanner id="08b69003-5fc2-4037-a479-93b440211c73"></create_task>" --host '+str(ipaddress))
    
    #use a script to run a certain script for vulnerability scan
    os.system('gvm-script --gmp-username name --gmp-password pass ssh --hostname <gsm> scripts/start-nvt-scan.gmp.py <oid of nvt> <target>')
    #requests pdf report of previous scan by report_id
    os.system('gvm-script --gmp-username name --gmp-password pass ssh --hostname <gsm> scripts/pdf-report.gmp.py <report_id> <pdf_file>')


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

if __name__ == "__main__":
    #user input using params
    #Command line arguments creation and declaration
    parser = argparse.ArgumentParser(prog='Disseration Toolkit', usage='[options]', formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=27))

    #args to use different functinos
    parser.add_argument('-L', action='store_true', required=False, help='Use Lynis')
    parser.add_argument('-B', action='store_true', required=False, help='Use BloodHound')
    parser.add_argument('-N', action='store_true', required=False, help='Use Nmap')

    #target information(nameserver for Bloodhound)
    parser.add_argument('-i', metavar=' [target]', required=True, help='IP address or address range to be tested')

    #file names (bloodhound might not be able to use this)
    parser.add_argument('-fN', metavar=' [file]', required=False, help='Name of the output file for Nmap')
    parser.add_argument('-fO', metavar=' [file]', required=False, help='Name of the output file for gvm')

    #bloodhound domain creds
    parser.add_argument('-bhU', metavar='[username]', required=False, help='Bloodhound account username')
    parser.add_argument('-bhP', metavar='[password]', required=False, help='Bloodhound account password')
    parser.add_argument('-bhD', metavar='[domain]', required=False, help='Bloodhound domain')

    args = parser.parse_args()
    ipaddress = args.i
    nmapFileName = args.fN
    bhUser = args.bhU
    bhPass = args.bhP
    bhDom = args.bhD

    if args.N:
        nmap(ipaddress, nmapFileName)

    if args.L:
        lynis(ipaddress)
    
    if args.B:
        bloodhound(ipaddress, bhUser, bhPass, bhDom)

    #makeEnumReport()


    