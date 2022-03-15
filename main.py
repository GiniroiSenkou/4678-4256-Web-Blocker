#########Easy Web Blocker by Giniroisenkou#########
###################################################
import time
import os
import platform

system = platform.system()
redirect_to_site = "127.0.0.1"


if system == "Linux":
    path_hosts = "/etc/hosts"
elif system == "Windows":
    path_hosts = "C:\Windows\System32\drivers\etc\hosts"
else:
    path_hosts = "/private/etc/hosts"

def read_hosts():
    var = open(path_hosts, encoding='utf-8').read()
    return var

try:
    site_file = open("links.txt", encoding='utf-8').readlines()
    print(f"\nCurrent Blocked Websites:\n{'-'*50}\n{read_hosts()}\n{'-'*50}")

except Exception as ERR:
    print(ERR)


insert_mode = input(f"You have a total of {len(site_file)} \"links\" on your links.txt \nWould you like to \"ADD\" or \"REMOVE\" to the filter?")

if insert_mode[0].lower() == "a":
    with open(path_hosts, 'r+') as file:
        content = file.read()
        for website in site_file:
            if website in content:
                pass
            else:
                file.write(redirect_to_site + "	" + website + "\n")

else:
    with open(path_hosts, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in site_file):
                file.write(line)
        file.truncate()


print(f"\n\nDone, These are the Blocked Websites:\n{'-' * 50}\n{read_hosts()}\n{'-' * 50}")



print("Note: You might need to flush your DNS if the change does not apply")
