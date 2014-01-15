from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import links_made
import re
import sys
import csv

from flipscrapy.items import FlipscrapyItem



items = []

class DmozSpider(BaseSpider):
    name = "flipkart"
    allowed_domains = ["flipkart.com"]
    start_urls = links_made.main()

    '''start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]'''

    def parse(self, response):

        item = FlipscrapyItem()

        sel = Selector(response)

        img_tag = sel.xpath('//*[@id="visible-image-small"]').extract()
        img_url = re.findall(r'src=[\'"]?([^\'" >]+)',str(img_tag[0]))
        img_url = img_url[0]

        item_title = sel.xpath("/html/body/div/div[2]/div/div[2]/div[3]/div/div/div[3]/div/h1/text()").extract()
        item_title = str(item_title[0]).strip()

        item_price = img_item = sel.xpath("/html/body/div/div[2]/div/div[2]/div[3]/div/div/div[3]/div[2]/div/div/div/div/span/text()").extract()
        item_price = str(item_price[0]).strip()

        item_discount = sel.xpath("/html/body/div/div[2]/div/div[2]/div[3]/div/div/div[3]/div[2]/div/div/div/span[2]/text()").extract()
        try:
            item_discount = str(item_discount[0]).strip()
        except:
            item_discount = "None"

        seller_name = sel.xpath("/html/body/div/div[2]/div/div[2]/div[3]/div/div/div[3]/div[2]/div[2]/div/div/a/text()").extract()
        seller_name = str(seller_name[0]).strip() 

        item["img_url"] = img_url 
        item["item_title"] = item_title  
        item["item_price"] = item_price
        item["item_discount"] = item_discount
        item["seller_name"] = seller_name
        items.append(item)
        
        f = open("pandent.csv", "a+")
        print >>f, ','.join(item.values())
        f.close()

        return items




