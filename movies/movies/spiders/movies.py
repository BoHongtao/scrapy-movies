import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from movies.items import MoviesItem
class Myspider(scrapy.Spider):
    # http://www.ygdy8.net/html/gndy/dyzz/list_23_2.html
    # name是爬虫的名字，执行scrapy时会用到
    name = "movies"
    allowed_domains = ['ygdy8.net']
    base = "http://www.ygdy8.net"
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_'
    base_end = '.html'

    # 每一页
    def start_requests(self):
        print("开始执行爬虫")
        for i in range(1, 10):
            url = self.base_url + str(i) + self.base_end
            yield Request(url, self.parse)

    #每一页的每一个
    def parse(self, response):
        tables = BeautifulSoup(response.text,'lxml').findAll('table',class_='tbspan')
        for table in tables:
            movie_name = table.find('a', class_='ulink').get_text()
            movie_info = table.findAll('tr')[-1].find('td').get_text()
            movie_info_url = self.base + table.find('a', class_='ulink')['href']
            yield Request(movie_info_url,callback=self.getdownurl,meta={'name':movie_name,'info':movie_info})

    # 获取每一页的详情和下载链接
    def getdownurl(self,response):
        item = MoviesItem()
        download_url = BeautifulSoup(response.text,'lxml').find('div',class_='co_content8').find('table').find('tbody').find('tr').find('td').find('a')['href']
        item['movie_download'] = download_url
        item['movie_name'] = response.meta['name']
        item['movie_info'] = response.meta['info']
        return item