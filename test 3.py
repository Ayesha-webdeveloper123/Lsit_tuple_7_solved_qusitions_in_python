#list of 5 number 
list=[35,15,20,25,30]
if list[0]>list[-1]:
    print("the number is greater than the last number")
else:
    print("the number is not greatr than the last number")

 #tuple containing 5 number check number is exist
tuple=(10,15,20,25,30)
number=int(input("enter the number:"))
if number in tuple:
    print("number is exist in tuple")
else:
    print("number is not exist in tuple")

        #length greater than 10 or not
string=input("enter a string:")
if len(string)>10:
    print("length is greater than 10")
else:
    print("length is not greater than 10")

    #tuple of 5 names take a name from user and check that is exist in tuple
tuple=("ayesha","samavia","eshwa","areeba" ,"sadia" )
name=input("enter the name:")
if name in tuple:
    print("name is present")
else:
    print("name is not present")

#check string it strt with a
string=input("enter the string:")
if string .startswith ("A"):
    print("string start with A")
else:
    print("string not start with A")

 #SUM OF TWO NUMBER IN LIST
list=[10 ,20,30,40,50]
sum=list[0]+list[1]
if sum>20:
    print("yes")
else:
    print("no")

    #palidorome is or not
string=("enter the string:")
if string==string[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")


    
