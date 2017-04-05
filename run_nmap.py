
import os

def run_nmap(arg, url):

    command = 'nmap ' + arg + ' ' + url
    process = os.popen(command)
    results = str(process.read())
    return results

print(run_nmap('-F', '54.186.250.79'))
