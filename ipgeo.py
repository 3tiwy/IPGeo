#python
#simple ip Geolocation tool using api
#3tiwy
import os
import requests
os.system(pip3 install requests)
class c:
    HE = '\033[6m'
    A = '\033[1m'
    C = '\033[63m'
    OKGREEN = '\033[4m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    E = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(c.WARNING+"""
    ##########################################
    ##      IP Geolocation                  ##
    ##                               v1.0   ##
    ## by Ahmed 3tiwy                       ##
    ##########################################
"""
    +c.E)
p=input("Enter the IP >" )
url=("https://api.ipgeolocation.io/ipgeo?apiKey=2804d60b250245ce918b4e38085abe66&ip=")
r = requests.get(url+p)
x=r.json()
print(c.A+"ip > "+c.E+x['ip'])
print(c.A+"continent > "+c.E+x['continent_name'])
print(c.A+"country > "+c.E+x['country_name'])
print(c.A+"city > "+c.E+x['city'])
print(c.A+"latitude > "+c.E+x['latitude'])
print(c.A+"longitude > "+c.E+x['longitude'])
print(c.A+"isp > "+c.E+x['isp'])
print(c.A+"connection type > "+c.E+x['connection_type'])
