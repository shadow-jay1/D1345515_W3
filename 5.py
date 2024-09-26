string=int(input('輸⼊三位數：'))
a=int(string//100)
b=int(string//10)-a*10
c=int(string%10)
print(c,b,a,sep='')