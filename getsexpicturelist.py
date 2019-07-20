# utf-8
import requests
# from connectDB import cursor_datas
from bs4 import BeautifulSoup, UnicodeDammit
import os
import re
import random
from random import choice
#import pymysql
import sys
import json
sys.path.append('../')


def open_url2(url):
    # heads = {}
    # heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    # req = requests.get(url, headers=heads).content
    # return req
    UserAgent = [
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
        'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
        'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
        'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
        'Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13'
    ]
    user_agent = choice(UserAgent)
    headers = {'User-Agent': user_agent}
    
    html = requests.get(url, headers=headers).content
    return html

def open_url(url,arr):
    # heads = {}
    # heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    # req = requests.get(url, headers=heads).content
    # return req
    UserAgent = [
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
        'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
        'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
        'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
        'Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13'
    ]
    user_agent = choice(UserAgent)
    headers = {'User-Agent': user_agent}
    
    html = requests.get(url, headers=headers).content
    find_href(html,arr)


def find_href(req,arr):
    soup = BeautifulSoup(req, 'lxml')
    hreflist = []
    for each in soup.find_all('tr', class_='tr3 t_one'):

        links = each.a.get('href')
        # print(links)
        #pattern = r'(html_data/[^"]+\.html)'
        pattern = r'^html_data/.*\.html$'
        R = re.findall(pattern,links)
        # print(R)
        for i in R:
            href = "http://jinwandafiji.top/pw/" + i
            print(href)
            if href:
                hreflist.append(href)
    # return hreflist
    find_img(hreflist,arr)

def find_img(hreflist,arr):
    print(len(hreflist))
    #datalist = []
    titlelist = []
    alldatas=[]
    # dbname = sex_picture
    # db_name = 'sex_picture'
    for i in hreflist:
        html = open_url2(i)
        srclist = []
        soup = BeautifulSoup(html, 'lxml')
        souph1 = soup.find('h1')
        if souph1:
            titles = souph1.get_text().strip()
            title = titles.replace('[','').replace(']','')
        else:
            print("network error")
        #cursor.execute("DROP TABLE IF EXISTS `"+title+"`")
        # sql = """CREATE TABLE IF NOT EXISTS `"""+title+"""`(
        # ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        # href CHAR(100) NOT NULL,
        # likenumber INT,
        # collect INT,
        # see INT
        # )"""
           
        # cursor_datas(sql,db_name)
        
        #strip去除多余的空格(\n)
        titlelist.append(title.strip())
        for each in soup.select('div[class=f14] > img'):      
            src = each.get('src').strip()
            # print(src)
            srclist.append(src)
        alldata={'title':title,'href':srclist,'star':0 ,'collect':False,'delete':False,'download':False}
        alldatas.append(alldata)
        #print(alldata)
    arr += alldatas
    
        # for e in srclist:
            
        #     data = "INSERT IGNORE INTO `"+title+"`(`href`,`likenumber`,`collect`,`see`) VALUES ('"+str(e)+"',0,0,0);"
                    
        #     cursor_datas(data,db_name)


def urllist(url,arr):
    urllist=[]
    for i in range(1,3):
        newurl = url + "&page="+str(i)
        urllist.append(newurl)
        print(newurl)
        open_url(newurl,arr)

def save_json(arr):
    newfile = open('sexpicturehref.json','a',)
    newfile.write(json.dumps(arr))
    newfile.close()

def sumarr(url):
    arr = []
    urllist(url,arr)
    save_json(arr)
    print(len(arr))



# def urlarr():
#     urlarr = ['http://k6.csnmdcjnx.pw/pw/thread.php?fid=114','http://k6.csnjcbnxdnb.xyz/pw/thread.php?fid=14' ]
#     for url in urlarr:
#         sumarr(url)


if __name__ == '__main__':
    # sexbeauty
    url = 'http://jinwandafiji.top/pw/thread.php?fid=14'
    #  clear beauty
    # url = 'http://k6.csnjcbnxdnb.xyz/pw/thread.php?fid=14' 
    # find_img(find_href(open_url(url)))
    sumarr(url)