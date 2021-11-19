n=int(input())
for i in range(1,1+n//2): #(1,3)
 if(n==i*i): #4==2*2
  print('perfect square')
  break
else:
 print('not a perfect square')