string=int(input('請輸⼊⼀個五位數：'))
a=int(string//10000)
b=int(string//1000)-a*10
c=int(string//100)-a*100-b*10
d=int(string//10)-a*1000-b*100-c*10
e=int(string%10)
print(a,b,c,d,e,sep='\n')