a , n = 0,1
# max is one-tresexagintillion
max="1"+("0"*192)
max=int(max)
while n < max:
    print(n)
    a,n = n,a+n
