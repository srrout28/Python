n=int(input('enter valur to generate factor list:'))
factor=[i for i in range(1,9) if n%i==0]
print("number of factors",len(factor))
print(factor)
