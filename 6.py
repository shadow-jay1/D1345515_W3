a=float(input('輸入係數a:'))
b=float(input('輸入係數b:'))
c=float(input('輸入係數c:'))
cheak=float(b**2-4*a*c)
ans1=float((-b+cheak**0.5)/(2*a))
ans2=float((-b-cheak**0.5)/(2*a))
print('方程式的解為:',ans1,ans2,sep='\n')