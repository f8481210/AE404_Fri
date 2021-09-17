from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
import requests,random
from bs4 import BeautifulSoup
from linebot.models import (
        MessageEvent, TextMessage, TemplateSendMessage, CarouselColumn,
        ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,CarouselTemplate,URIAction,
        MessageAction, ButtonsTemplate, TextSendMessage)


app = Flask(__name__)

line_bot_api = LineBotApi('channel access token')
handler = WebhookHandler('channel secret')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

def thisweek_new_movie():
    url = "https://movies.yahoo.com.tw/movie_thisweek.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    content=[]
    movieNames = soup.find_all('div',class_='release_movie_name')
    trailerUrls = soup.find_all('div',class_='release_btn color_btnbox')
    imgSrcs = soup.find_all('div',class_='release_foto')
    for movie in range(len(movieNames)):
        name = movieNames[movie].find('a').text.strip()
        try:
            trailerUrl = trailerUrls[movie].find_all('a')[1]['href']
        except:
            continue
        imgSrc = imgSrcs[movie].find('img')['src']
        content.append(name)
        content.append(trailerUrl)
        content.append(imgSrc)
    return content

def MovieRank(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    first = soup.find("dl",class_="rank_list_box").find('h2').text
    movie_rank='第1名:'+first+'\n'
    for rank,movie in enumerate(soup.find_all("div",class_="rank_txt")):
        movie_rank += '第{}名:{}\n'.format(str(rank+2),movie.text)
    return movie_rank

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "Button":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/xyPtn4m.jpeg',
                title='按鈕樣板練習',
                text='請選擇',
                actions=[
                    MessageAction(
                        label='AE404',
                        text='聊天機器人'
                    ),
                    URITemplateAction(
                        label='猿創力官網',
                        uri='https://www.codingapeschool.com/'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
    if event.message.text == "猿創力":
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://codingapeschool.com/storage/images/v3/learnMap/learnMap.jpg',
                        title = "菁英課程",
                        text='適合對象：國小五年級以上',
                        actions=[URIAction(
                                label='Python 常態班',
                                uri='https://www.codingapeschool.com/courses-python'
                        ),
                            MessageAction(
                                label='可以學到什麼?',
                                text='1.Python程式設計輕鬆學\n2.創造自己的聊天機器人\n3.學會數據資料擷取神功'
                    )]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://codingapeschool.com/storage/images/v3/learnMap/learnMap.jpg',
                        title = "創造課程",
                        text='適合對象：國小三～六年級',
                        actions=[
                            URIAction(
                                label='Scratch程式AI機器人',
                                uri='https://www.codingapeschool.com/courses-scratch'
                        ),
                            MessageAction(
                                label='可以學到什麼?',
                                text='1.自己動手實踐創意\n2.運用程式操控機器人\n3.創造思考學習模式'
                    )]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    
    if event.message.text == "新片":
        movie = thisweek_new_movie()
        name=[]
        trail=[]
        poster=[]
        for i in range(0,len(movie),3):
            name.append(movie[i])
            trail.append(movie[i+1])
            poster.append(movie[i+2])
        mix=[]
        keys=['name','trail','poster']
        mix.append(name)
        mix.append(trail)
        mix.append(poster)
        dictionary=dict(zip(keys,mix))
        p=random.sample(range(len(name)),3)
        Image_Carousel = TemplateSendMessage(
        alt_text='目錄 template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url=dictionary['poster'][p[0]],
                action=URITemplateAction(
                    uri=dictionary['trail'][p[0]],
                    label=dictionary['name'][p[0]]
                )
            ),
            ImageCarouselColumn(
                image_url=dictionary['poster'][p[2]],
                action=URITemplateAction(
                    uri=dictionary['trail'][p[2]],
                    label=dictionary['name'][p[2]]
                )
            ),
            ImageCarouselColumn(
                image_url=dictionary['poster'][p[1]],
                action=URITemplateAction(
                uri=dictionary['trail'][p[1]],
                label=dictionary['name'][p[1]]
                )
            )
            ]))
        line_bot_api.reply_message(event.reply_token,Image_Carousel)
    if event.message.text == "排行":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/a5MK3cu.jpeg',
                title='Yahoo電影排行榜',
                text='請選擇',
                actions=[
                    MessageAction(
                        label='台北排行榜',
                        text='台北排行榜'
                    ),
                    MessageAction(
                        label='全美排行榜',
                        text='全美排行榜'
                    ),
                    MessageAction(
                        label='年度排行榜',
                        text='年度排行榜'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    if event.message.text == "台北排行榜":
        taipei_movie_rank = MovieRank("https://movies.yahoo.com.tw/chart.html")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=taipei_movie_rank))
    if event.message.text == "全美排行榜":
        usa__movie_rank = MovieRank("https://movies.yahoo.com.tw/chart.html?cate=us")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=usa__movie_rank))
    if event.message.text == "年度排行榜":
        year_movie_rank = MovieRank("https://movies.yahoo.com.tw/chart.html?cate=year")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=year_movie_rank))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)