#make a file friuts.txt write fruit names
fruits=["apple\n","orange\n","grapes\n","watermelon"]
file=open("fruits.txt","w")
file.writelines(fruits)
