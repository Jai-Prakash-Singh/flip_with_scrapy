#!/usr/bin/env python 

# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

import proxy_module
import firebug_proxy
from bs4 import BeautifulSoup 
import multiprocessing
import time




class parse(object):

    def __init__(self, cat_title, cat_link):
        self.link = cat_link
        self.cat_title = cat_title

    def scroll(self):
        self.page, self.driver = firebug_proxy.main(self.link)

        for i in range(0,25):
	    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        loop =  True
     
        while loop is True:
            try:
                elem = self.driver.execute_script("window.scrollBy(0,-450)", "");
                time.sleep(2)
                elem = self.driver.find_element_by_id("show-more-results")
                elem.click()   
                time.sleep(2)  
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            except:
                loop = False

        self.page = self.driver.page_source
        self.driver.close()

        return self.page 

        



   
       
def open_page(cat_link, cat_title):

    obj = parse(cat_title, cat_link)
    page = obj.scroll()

    filename = cat_title+"code.html"
    f = open(filename,"w+")
    print >>f, page.encode("ascii", "ignore")



        



def jwellery():

    main_link = "http://www.flipkart.com/jewellery"

    page = proxy_module.main(main_link)
    soup = BeautifulSoup(page)
    cat_available = soup.find_all("div", attrs={"id":"list-categories"})
    all_links = cat_available[0].find_all("a")

    jobs = []
    for l in all_links:
        cat_link = "http://www.flipkart.com/"+ str(l.get("href"))
        cat_title = str(l.get_text()).strip()
        p = multiprocessing.Process(target=open_page, args = (cat_link, cat_title))
        p2 = multiprocessing.Process(target=open_page, args = (cat_link, cat_title))
        jobs.append(p)
        p.start()
    
    
            
            
if __name__=="__main__":
    jwellery()
