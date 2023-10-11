import scrapy
from scrapy import Selector
from GameTradeList7881.items import Gametradelist7881Item


class TradeListSpider(scrapy.Spider):
    name = 'trader_list'
    allowed_domains = ['account.7881.com']
    start_urls = ['https://account.7881.com/game/list']

    # step1-获取页面下所有的游戏以及链接
    def parse(self, response):
        selector = Selector(response)
        cur_url=response.url
        p = selector.xpath("//div[@class='gameList']")
        for p_tmp in p:
            game_name = p_tmp.xpath("./dl/dd/p/text()").extract_first() # 游戏名称
            game_url=p_tmp.xpath("./dl/dt/a/@href").extract_first() # 游戏页面
            print(game_url)
            yield scrapy.Request('https:' + game_url, callback=self.parse_game_list, meta={'game_name': game_name,'cur_url':cur_url,'game_url':'https'+ game_url})

    # 获取每个游戏的翻页链接
    def parse_game_list(self,response):
        selector = Selector(response)
        cur_url = response.url
        p = selector.xpath("//div[@class='laypage_main laypageskin_default']/a[@class='laypage_next']")
        if '下一页' in p.xpath("./text()").extract():
            game_trade_list_url=p.xpath("./a/@href").extract()[1]
            yield Requests("https://search.7881.com/" + self.game_trade_list_url,callback=self.parse_trade_list)


    # 获取每个游戏每个翻页的交易列表
    def game_trade_list_url(self,response):
        selector=Selector(response)
        items=Gametradelist7881Item()
        for trade in selector.xpath("//div[@class='list-box list-type-03']/div/div[@class='list-item-box']/div/div/h2/a/em/@title").extract():
            items['title']=trade[0]
        yield items