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
    movie_rank='???1???:'+first+'\n'
    for rank,movie in enumerate(soup.find_all("div",class_="rank_txt")):
        movie_rank += '???{}???:{}\n'.format(str(rank+2),movie.text)
    return movie_rank

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "Button":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/xyPtn4m.jpeg',
                title='??????????????????',
                text='?????????',
                actions=[
                    MessageAction(
                        label='AE404',
                        text='???????????????'
                    ),
                    URITemplateAction(
                        label='???????????????',
                        uri='https://www.codingapeschool.com/'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
    if event.message.text == "?????????":
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://codingapeschool.com/storage/images/v3/learnMap/learnMap.jpg',
                        title = "????????????",
                        text='????????????????????????????????????',
                        actions=[URIAction(
                                label='Python ?????????',
                                uri='https://www.codingapeschool.com/courses-python'
                        ),
                            MessageAction(
                                label='???????????????????',
                                text='1.Python?????????????????????\n2.??????????????????????????????\n3.??????????????????????????????'
                    )]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://codingapeschool.com/storage/images/v3/learnMap/learnMap.jpg',
                        title = "????????????",
                        text='????????????????????????????????????',
                        actions=[
                            URIAction(
                                label='Scratch??????AI?????????',
                                uri='https://www.codingapeschool.com/courses-scratch'
                        ),
                            MessageAction(
                                label='???????????????????',
                                text='1.????????????????????????\n2.???????????????????????????\n3.????????????????????????'
                    )]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    
    if event.message.text == "??????":
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
        alt_text='?????? template',
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
    if event.message.text == "??????":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/a5MK3cu.jpeg',
                title='Yahoo???????????????',
                text='?????????',
                actions=[
                    MessageAction(
                        label='???????????????',
                        text='???????????????'
                    ),
                    MessageAction(
                        label='???????????????',
                        text='???????????????'
                    ),
                    MessageAction(
                        label='???????????????',
                        text='???????????????'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    if event.message.text == "???????????????":
        taipei_movie_rank = MovieRank("https://movies.yahoo.com.tw/chart.html")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=taipei_movie_rank))
    if event.message.text == "???????????????":
        usa__movie_rank = MovieRank("https://movies.yahoo.com.tw/chart.html?cate=us")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=usa__movie_rank))
    if event.message.text == "???????????????":
        year_movie_rank = MovieRank("https://movies.yahoo.com.tw/chart.html?cate=year")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=year_movie_rank))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)