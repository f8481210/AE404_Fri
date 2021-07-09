html_sample = '''
<html>
<head>
<title>Story</title>
</head>
<body>
<a href="www.a.com" class="L" >A</a>
<p class="story">在很久以前，有一個國家叫猿創力</p>
<a href="www.b.com" class="I">B</a>
</body>
</html>'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_sample,'html.parser')

#print(soup) #印出soup裡面的內容
#print(soup.prettify()) #印出有縮排後的內容
#print(soup.title) #取出title標籤並印出
print(soup.a) #取出a標籤並印出
#print(soup.a.attrs) #取出a標籤的屬性
#print(soup.p.text) #取出p標籤的內容


#print(soup.find('p'))
#print(soup.find_all(class_='L'))
#print(soup.find_all('a'))
#print(soup.find_all(href="www.b.com"))