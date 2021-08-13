'''
題目：取前100筆資料，顯示商品名稱和價錢。
'''
#匯入函式庫
import requests 

#count 可以得知 一頁有20筆資料
count = 0

pageNumber=1
while pageNumber <2:
#while pageNumber <: #要100筆資料，條件？
    
                        #https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=1&sort=sale/dc format(要插入字串{}裡的值)
    res = requests.get("https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page={}&sort=sale/dc".format(pageNumber))
    pageNumber+=1
    
    #json資料轉換成python格式
    res = res.json()['prods']
    
    for eachProduct in res:
        productName = eachProduct['name']
        productPrice = eachProduct['price']
        #print(productName,productPrice)
        count+=1
print(count)

        