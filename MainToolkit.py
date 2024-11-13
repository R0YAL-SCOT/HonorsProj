#Penetration testing toolkit
#Author: Andrew Walker
#my comment!

import os

def main():
    nmap()
    


def nmap():
    runNmap='nmap --open -A -Pn -sT -T'+str()+' '+str()+' -oX '+chr(34)++chr(34)

    print(runNmap)
    exit_code = os.system(runNmap)
    exit_status = exit_code >> 8
    if exit_status:
        print("ERROR: Nmap failed to run")
    exit(1)

    print("Info: Output can be found in " + filename)

