# _*_coding:utf-8 _*_

# @Time      : 2021/12/15  14:13
# @Author    : An
# @File      : game_account_info.py
# @Software  : PyCharm

import requests, json
from lxml import etree

import requests, json, time
from lxml import etree

from UserAgent import get_useragent_list
import numpy as np
import pandas as pd

useragent_list =get_useragent_list()
print(np.random.choice(useragent_list))
df= pd.DataFrame()

def account_trade_games():
    # 获取账号交易的游戏
    url = 'https://account.7881.com/game/list'

    data = {
        'gameType': '',
        'hotFlag': 'hot',
        'px': ''
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json;charset=UTF-8',
        'Connection': 'keep-alive',
        'User-Agent': np.random.choice(useragent_list),
        'Host': 'account.7881.com',
        'Origin': 'https://account.7881.com',
        'Referer': 'https://account.7881.com/top/'
    }
    res = requests.post(url, headers=headers, data=json.dumps(data),timeout=(3,7))

    return res.text


def trading_list(init_page_num, game_id):
    # 获取游戏的账号列表
    account_url = 'https://search.7881.com/list.html?pageNum={0}&gameId={1}&gtid=100003&instock=false&tagValue=0'.format(init_page_num, game_id)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Connection':'keep-alive',
        'Host': 'search.7881.com',
        'User-Agent':np.random.choice(useragent_list),


    }
    print(account_url)
    res = requests.get(account_url, headers=headers,timeout=(3,7))
    print(res.status_code)
    content = res.text
    html = etree.HTML(content)
    parse_trade_info(html)
    page_num_list = html.xpath("//div[@class='laypage_main laypageskin_default']/a/text()")
    if not page_num_list:
        print(content)
        return
    print(init_page_num,page_num_list)
    if '下一页' in page_num_list:
        init_page_num = init_page_num + 1
        time.sleep(10)
        trading_list(init_page_num, game_id)
    else:
        return


def parse_trade_info(html):
    trade_list = html.xpath("//div[@class='list-item']")
    for trade in trade_list:
        try:
            title = trade.xpath("./div[@class='list-item-box']/div/div[@class='txt-box']/h2/a/em/@title")[0]
        except:
            title = ''
        try:
            hot_num = trade.xpath(
                "./div[@class='list-item-box']/div/div[@class='txt-box']/h2/a/em[@class='hot-num']/text()")[0]
        except:
            hot_num = ''
        try:
            href = trade.xpath("./div[@class='list-item-box']/div/div[@class='txt-box']/h2/a/@href")[0]
        except:
            href = ''
        try:
            main_title = trade.xpath("./div[@class='list-item-box']/div/div[@class='txt-box']/h2/a/span/text()")[0]
        except:
            main_title = ''
        try:
            zone_type = trade.xpath("./div[@class='list-item-box']/div/div[@class='txt-box']/h4/i/text()")[0]
        except:
            zone_type = ''
        try:
            zone_name = trade.xpath("./div[@class='list-item-box']/div/div[@class='txt-box']/h4/span/text()")[0]
        except:
            zone_name = ''
        try:
            goods_type = trade.xpath("./div[@class='list-item-box']/div/div[@class='txt-box']/p[1]/i/text()")[0]
        except:
            goods_type = ''
        try:
            goods_name = trade.xpath("./div[@class='list-item-box']/div/div[@class='txt-box']/p[1]/span/text()")[0]
        except:
            goods_name = ''
        try:
            safe_type = trade.xpath("./div[@class='list-item-box']/div/div[@class='txt-box']/p[2]/i/text()")[0]
        except:
            safe_type = ''
        try:
            safe_star = trade.xpath("./div[@class='list-item-box']/div/div[@class='txt-box']/p[2]/span/@class")[0]
        except:
            safe_star = ''
        try:
            price = trade.xpath("./div[@class='list-item-box']/div[@class='list-v part-02']/h5/text()")[0]
        except:
            price = ''
        try:
            post_sale_type = trade.xpath(
                "./div[@class='list-item-box']/div[@class='list-v part-04']/div[@class='tags-box']/p[1]/a/text()")[0]
        except:
            post_sale_type = ''
        try:
            authen_type = trade.xpath(
                "./div[@class='list-item-box']/div[@class='list-v part-04']/div[@class='tags-box']/p[2]/a/text()")[0]
        except:
            authen_type = ''
        try:
            trade_status = trade.xpath("./div[@class='list-item-box']/div[@class='list-v part-05']/h5/a/text()")[0]
        except:
            try:
                trade_status = trade.xpath("./div[@class='list-item-box']/div[@class='list-v part-03']/h3/span/@class")[
                    0]
            except:
                trade_status = trade.xpath("./div[@class='list-item-box']/div[@class='list-v part-05']/h3/span/@class")[
                    0]

        trade_info = {
            'title': title.strip().replace('\n', '').replace('\r', ''),
            'hot_num': hot_num.strip().replace('\n', '').replace('\r', ''),
            'href': href.strip().replace('\n', '').replace('\r', ''),
            'main_title': main_title.strip().replace('\n', '').replace('\r', ''),
            'zone_type': zone_type.strip().replace('\n', '').replace('\r', ''),
            'zone_name': zone_name.strip().replace('\n', '').replace('\r', ''),
            'goods_type': goods_type.strip().replace('\n', '').replace('\r', ''),
            'good_name': goods_name.strip().replace('\n', '').replace('\r', ''),
            'safe_type': safe_type.strip().replace('\n', '').replace('\r', ''),
            'safe_star': safe_star.strip().replace('\n', '').replace('\r', ''),
            'price': price.strip().replace('\n', '').replace('\r', ''),
            'post_sale_type': post_sale_type.strip().replace('\n', '').replace('\r', ''),
            'authen_type': authen_type.strip().replace('\n', '').replace('\r', ''),
            'trade_status': trade_status.strip().replace('\n', '').replace('\r', '')
        }

        global  df
        df=df.append(trade_info,ignore_index = True)



if __name__ == '__main__':
    init_page_num, game_id = 1, 'G10'
    game_trading_list = trading_list(init_page_num=init_page_num, game_id=game_id)
    df.to_excel(r"C:\Users\Public\Desktop\trade.xlsx")
