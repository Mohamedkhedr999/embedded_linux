#!/usr/bin/python3
import requests



x=requests.get("https://www.boredapi.com/api/activity")
print(x.json()["activity"])