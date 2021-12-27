import urllib.request
import bs4

url = "http://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"list_nav"})

lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    print(a_tag)