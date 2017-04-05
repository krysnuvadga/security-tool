
import os
# function to get ip address
def get_ip_address(url):

    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12

    # get only top level ip address
    return results[marker:].splitlines()[0]

print(get_ip_address('facebook.com'))
print(get_ip_address('google.cm'))