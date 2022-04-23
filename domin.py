import requests
import colorama 

colorama.init()
gr = colorama.Fore.GREEN
reset = colorama.Fore.RESET
print (gr,""" [Running]

            _         _     
           | |       | |    
   ___ _ __| |_   ___| |__  
  / __| '__| __| / __| '_ \ 
 | (__| |  | |_ _\__ \ | | |
  \___|_|   \__(_)___/_| |_| - by : abdallahal3zy
                            
                                                                  
""",reset)

def get(domain):
     url = f"https://crt.sh/?q={domain}&output=json"
     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1",
                "Cache-Control": "max-age=0", "Te": "trailers"}
     requests.get(url, headers=headers)
     sendar = requests.get(url, headers=headers).json()
     file = open('subdomains.txt', 'w')
     for i in sendar:
        #print(gr,i['name_value'], reset)
        file1 = file.write(i['name_value']+'\n')
     return i

url = input('Enter domain Here => example.com <: ')
lines_seen = set(get(url))
with open("subdomains.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i not in lines_seen:
            f.write(i)
            lines_seen.add(i)
    f.truncate()
ss = open('subdomains.txt', 'r')
print(gr ,ss.read() ,reset)
ss.close()
