#Penetration testing toolkit
#Author: Andrew Walker

def nmap():
    runNmap='nmap --open -A -Pn -sT -T'+str(timing)+' '+str(ipaddress)+' -oX '+chr(34)+filename+chr(34)

    print(runNmap)
    exit_code = os.system(runNmap)
    exit_status = exit_code >> 8
    if exit_status:
        print("ERROR: Nmap failed to run")
    exit(1)

    print("Info: Output can be found in " + filename)

