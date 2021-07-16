#text = 'This is my first text'
#f = open('my file.txt', 'w')
#f.write(text)
#f.close()

file = open("minecraft.jpg", "rb")
img = file.read()
file.close()
print(img)

#圖片檔案複製
file = open("複製.jpg", "wb")
file.write(img)
file.close()

#可以試著print
#print(ppt)
