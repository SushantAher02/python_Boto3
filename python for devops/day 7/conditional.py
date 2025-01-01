import sys

type = sys.argv[1]

if type =="t2.micro":
    print("it will charge you 2 doller a day")
elif type=="t2.medium":
    print("it will charge you 4 doller a day")   
elif type=="t2.large":
    print("it will charge you 8 doller a day")       
else:
    print("something wrong")    
     
    