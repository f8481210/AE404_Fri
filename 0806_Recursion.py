# =============================================================================
# 題目:從0加到100的算法
# =============================================================================

#for迴圈
num = 0

for i in range(101):
    num += i
print(num)


#while迴圈
num = 0
count = 0
while count < 100:
    count += 1
    num += count
print(num)

#遞迴
def recursive(n):
    if n<0:
        return 0 
    #print('n:',n)
    return n +recursive(n-1)

print(recursive(100))

#階層
def recursive(n):
    if n<1:
        return 1 
    print('n:',n)
    print(n,'*',n-1,"!")
    return n *recursive(n-1)

print(recursive(5))