# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re 


def add(s):
    s = "http://www.flipkart.com"+s
    return s


def main():
    filename = "Pendants & Locketscode.html"
    f = open(filename)
    html = f.read().encode("ascii","ignore")
    soup = BeautifulSoup(html)
    links = soup.find_all("a", attrs={"class":"fk-display-block"})
    link_list = ', '.join(map(str, links))
    urls = re.findall(r'href=[\'"]?([^\'" >]+)', link_list)
    f.close()
    urls_list  = map(add, urls)
    return  urls_list 

    
if __name__=="__main__":
    urls_list = main()   


    





