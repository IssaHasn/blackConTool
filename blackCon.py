import urllib.parse
import requests
import socket
import re
from colorama import Fore, Back

def interface():
    title = '''
     _     _     _____ _____ _   _   _____ _____ _   _
    | |   | |   |  _  | ____| | / / | ____| ___ | | / |
    | |   | |   | | | | |   | |/ /  | |   | | | | |/  |
    | |___| |   | |_| | |   | / /   | |   | | | | | | |
    | ___ | |   |  _  | |   | \ \   | |   | | | | | | |
    | |_| | |___| | | | |___| |\ \  | |___| |_| |  /| |
    |_____|_____|_| |_|_____|_| \_\ |_____|_____|_/ |_|

    %$ Written by : Issa Hasn
    **********
    '''
    print(Fore.BLUE + title + Fore.RESET)

def extractDomainName(url):
    parsedUrl = urllib.parse.urlparse(url)
    return parsedUrl.netloc

def getIpByDomain(domain):
    host = socket.gethostbyname(domain)
    return host

def getIpByUrl(url):
    host = urllib.parse.urlparse(url).hostname
    addr = socket.gethostbyname(host)
    return addr

def is_link(variable):
    regex = r"(http|https)://[a-zA-Z0-9@:%._\\+~#?&//=]"
    return re.search(regex, variable) is not None

def checkCon():
    while True:
        url = input("Enter url you want to click it >>> ")

        if is_link(url):
            domain = extractDomainName(url)

            try:
                webIp = getIpByDomain(domain)
                urlIp = getIpByUrl(url)

                print(Fore.GREEN + 'Suspicious connections are checked ...' + Fore.RESET)
                print(webIp, ' :: ', domain)
                print(urlIp, ' :: ', url)
                if webIp == urlIp:
                    print(Fore.GREEN + f'[*] No risks in /////> {url}\n----------\n' + Fore.RESET)
                else:
                    print(Fore.YELLOW + f'[!] Ip for "{url}" not for this domain "{domain}"\n----------\n' + Fore.RESET)
            except:
                print(Fore.RED + "[!!!] Link not found \n----------\n" + Fore.RESET)
        else:
            print(Fore.RED + "[!!!] The entry is not a link \n----------\n" + Fore.RESET)

def main():
    interface()
    checkCon()

if __name__ == '__main__':
    main()