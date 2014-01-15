# Scrapy settings for flipscrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'flipscrapy'

SPIDER_MODULES = ['flipscrapy.spiders']
NEWSPIDER_MODULE = 'flipscrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'flipscrapy (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'flipscrapy.middlewares.ProxyMiddleware': 100,
}
