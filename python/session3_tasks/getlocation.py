#!/usr/bin/python3
import requests

myip = requests.get("https://api.ipify.org/?format=json")
mylocation = requests.get("https://ipinfo.io/"+myip.json()["ip"]+"/geo")
print(mylocation.json())