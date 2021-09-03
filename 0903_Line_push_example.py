from linebot import LineBotApi
from linebot.models import TextSendMessage,StickerSendMessage,LocationSendMessage,VideoSendMessage,AudioSendMessage,ImageSendMessage
line_bot_api=LineBotApi('Your_Channel_Access_Token')
UserID='Your_UserID'

#文字訊息
text_message=TextSendMessage(text='hello world!')
line_bot_api.push_message(UserID,text_message)

'''
#貼圖訊息
sticker_message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
)
line_bot_api.push_message(UserID,sticker_message)


#圖片訊息
image_message = ImageSendMessage(
    original_content_url='https://i.imgur.com/xyPtn4m.jpeg',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg'
)
line_bot_api.push_message(UserID,image_message)


#位置訊息
location_message = LocationSendMessage(
    title='CodingAPE猿創力程式設計學校',
    address='台北市信義區基隆路一段180號',
    latitude=25.042408,
    longitude=121.564839)
line_bot_api.push_message(UserID,location_message)


#影片訊息
video_message = VideoSendMessage(
    original_content_url='https://i.imgur.com/oRcIXiM.mp4',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg'
)
line_bot_api.push_message(UserID,video_message)

#多種訊息傳送
message = [video_message,text_message,sticker_message,location_message,image_message]
line_bot_api.push_message(UserID,message)
'''


