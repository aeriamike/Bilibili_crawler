"""
import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            tet = link.get('title')
            print(tet)
            tet_2 = link.get('href')
            print(tet_2)
web(1,'http://www.amazon.in/s/ref=s9_acss_bw_cts_VodooFS_T4_w?rh=i%3Aelectronics%2Cn%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_98%3A10440597031%2Cp_36%3A1500000-99999999&bbn=1805560031&rw_html_to_wsrp=1&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=2EKZMFFDEXJ5HE8RVV6E&pf_rd_t=101&pf_rd_p=c92c2f88-469b-4b56-936e-0e65f92eebac&pf_rd_i=1389432031')
"""

import requests
import re
from bs4 import BeautifulSoup
url = 'http://api.bilibili.com/archive_stat/stat?aid=170001'
code = requests.get(url)
plain = code.text
print(plain)


groups = re.findall(r'\d+', plain)

print(groups)

print ("Bilibili video id: " + groups[3])
print ("View: " + groups[4])
print ("Danmaku: "+ groups[5])
print ("Reply comments: "+ groups[6])
print ("Favourite people: "+ groups[7])
print ("All Comments Liked: "+ groups[8])
print ("All Comments Disliked: "+ groups[9])



#template
#find followers list
#http://api.bilibili.com/x/relation/followers?vmid= (put bilibili user id here)

#find mid following follower
#https://api.bilibili.com/x/relation/stat?vmid= (put bilibili user id here)

#find video info
#http://api.bilibili.com/archive_stat/stat?aid= (put video id here)





