fname=input('enter name of file:')
f=open(fname,"r")
lst=f.readlines()
print('no of lines:',len(lst))
