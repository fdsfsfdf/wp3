from flask import Flask, render_template
from bs4 import BeautifulSoup
# from selenium import webdriver
import time
import requests
import random


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,"html.parser")
    return soup

def naverPolitics_news(i):
    url = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day"
    soup=create_soup(url)
    updatedNews = soup.find('div','ranking_section').find("li",f"num{i}").find('div','thumb').find('a')
    desc = soup.find('li',f'num{i}').find('dl').find('dd').find('span','lede').get_text()
    # print(updatedNews)
    title = updatedNews['title']
    # print(title)
    link = "https://news.naver.com" + updatedNews["href"]
    # print(link)
    img = updatedNews.find("img")['src']
    # print(img)
    return title,link,img,desc

def naverOther_news():
    url = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day"
    soup=create_soup(url)
    updatedNewsList = soup.find_all('div','ranking_section othbor')
    
    other_title = []
    other_link = []
    other_img = []
    other_desc = []
    for i in range(5):
        otherNews = updatedNewsList[i].find('li','num1').find('div','thumb').find('a')
        other_title.append(otherNews['title'])
        other_link.append("https://news.naver.com" + otherNews["href"])
        other_img.append(otherNews.find('img')['src'])
        other_desc.append(updatedNewsList[i].find('li','num1').find('dl').find('dd').find('span','lede').get_text())
    return other_title,other_link,other_img,other_desc

# 2 - 경제, 3 - 사회, 4- 생활/문화, 5- 세계, 6 - IT/과학

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index1.html'
    # naver_title1 = naverPolitics_news(1)[0],
    # naver_src1 = naverPolitics_news(1)[1],
    # naver_img1 = naverPolitics_news(1)[2],
    # naver_desc1 = naverPolitics_news(1)[3],

    # naver_title2 = naverOther_news()[0][0],
    # naver_src2 = naverOther_news()[1][0],
    # naver_img2 = naverOther_news()[2][0],
    # naver_desc2 = naverOther_news()[3][0],
    
    # naver_title3 = naverOther_news()[0][1],
    # naver_src3 = naverOther_news()[1][1],
    # naver_img3 = naverOther_news()[2][1],
    # naver_desc3 = naverOther_news()[3][1],
    
    # naver_title4 = naverOther_news()[0][2],
    # naver_src4 = naverOther_news()[1][2],
    # naver_img4 = naverOther_news()[2][2],
    # naver_desc4 = naverOther_news()[3][2],
    
    # naver_title5 = naverOther_news()[0][3],
    # naver_src5 = naverOther_news()[1][3],
    # naver_img5 = naverOther_news()[2][3],
    # naver_desc5 = naverOther_news()[3][3]
    )
    # time.sleep(random.randrange(1,120))

if __name__ == '__main__':
    #아마존 실행용
    # app.run('0.0.0.0',port=5000,debug=True)
    #내부실행용
    app.run(debug=True)