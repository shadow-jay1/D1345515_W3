string=int(input('請輸⼊⼀個三位數：'))
a=int(string//100)
b=int(string//10)-a*10
c=int(string%10)
print('每位數字的總和：',a+b+c,sep='')