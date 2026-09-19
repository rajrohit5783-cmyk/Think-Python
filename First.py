# # # # # # # Name = "Rohit"
# # # # # # # print(id(Name))
# # # # # # # Name = "Rohan"
# # # # # # # print(id(Name))

# # # # # # # A = 9.6
# # # # # # # print(id(A))
# # # # # # # A = 9.6
# # # # # # # print(id(A))

# # # # # # # B = input('Enter Your Name: ')
# # # # # # # print(B)
# # # # # # # print(type(B))

# # # # # # # C = int(input('Enter Your No: '))
# # # # # # # print(C)
# # # # # # # print(type(C))
# # # # # # D = int(float(input('Enter Your Number: ')))
# # # # # # # D = bool(input('Enter Your Number: '))
# # # # # # E = D + 10
# # # # # # print(E)
# # # # # # print(type(E))
# # # # # for a in range(5,16):
    # print(a)

# # # # a = 15
# # # # while(a<=30):
# # # #     print(a)
# # # #     a += 1
# # # A = int(input("Enter The Number: "))
# # # B = input("Enter Your Name: ")
# # # C = 1

# # # # while(A >= C):
# # # #     print(B)
# # # #     A -= 1



# # A = int(input('Enter The Number: '))

# # # for b in range(1,11):
# # #     print(A , "X" , b , "=" , A * b)
# # #     b+=1
 
 
# # b = 1
# # while(b<=10):  
# #    print(A , "X" , b , "=" , A * b)
# #    b+=1

# S = 0
# i = 1
# # for i in range(1,21):
# #     S= S+i
# #     print(S)
    
    

# while(i<=20):
#   S = S+i
#   print(S)
#   i+=1


# age = float(input("Enter Your Age: "))

# if age >= 18:
#     print("You are eligible for voting")
# else:
#     print("You are not eligible for voting")


# a = float(input("Enter the number: "))

# if a > 0:
#     print("Number is Positive")
# elif a < 0:
#     print("Number is Negative")
# else:
#     print("Neither the number is Positive nor Negative")


# a = 10
# b = 20
# c = 5

# if a > b and a>c:
#     print("a is greatest")
# elif b>a and b>c:
#     print("b is greatest")
# else:
#     print("C is greatest")

# def greet():
#     print("Good Night Rohit")

# greet()
# greet()
# greet()


# def greet(Name):
#     print("Good Morning " +  Name)

# greet("XYZ")

# def printname():
#     print("Hello world")
   
# printname() 


# def squarenumber(a):
#     return a*a
# result = squarenumber(3)

# new_result = result - 2

# print(new_result)

# print(result)



# def getName():
#    name =  input("Enter your name: ")
#    return name

# userName = getName()
# print(userName.upper())
# print(userName)


# output = lambda a,b,c : a + b + c
# print(output(3, 4, 5))

# B = lambda name: name.upper()
# print(B("rohit"))

# def printName(name,age):
#     return f"My name is {name}, and my age is {age}"

# print(printName("rohit","20"))
# print(f"My name is {printName('Rohit')}")

# name = input("Enter Your Name: ")
# age = int(input("Enter Your age: "))

# # print("My name is ", name ,"and age is ", age)
# print(f"My name is {name}, and my age is {age}")


# def add(a,b):
#     return a+b

# a = add(2,3)

# def mul():
#     return a * 2

# print(mul())


# def par():
    
#     def chi():
#         print("Inside the fn")
        
#     chi()

# par()


# def greet():
#     return "Good morning"

# def dis_gr(function):
#     print(function)
    
# dis_gr(greet())


# name = ["Rohit" , "Mihika" , "Ansh" , 23.89 , 8 , True ]
# print(name)

# print(name[3])
# print(name[-2])
# print(type(name[5]))

# print(name[-4:-1])

# name.append(False)
# print(name)

# name.insert(3,"Abhinav")
# print(name)

# n = 0
# Marks =[]
# A= int(input("Enter Your marks: "))
# # Marks.append(A)
# Marks.insert(2,A)
# print(Marks)

# print(Marks[0])

# while(n<=5):
#     A= int(input("Enter Your marks: "))
#     B= int(input("Enter the index "))
#     Marks.insert(B,A)
#     n+=1
# print(Marks)
# print(type(Marks))

# name1 = ["Rohit" , "Mihika" , "Ansh" , 23 , 8 ]
# name1[-1:-2] = 2
# print(name1)

# data = [16,19,25]

# for x in data:
#     print(data[x])


# data = [10,12,25,30]
# data = "Rohit"
# data = (10,23,34)
# it = iter(data)

# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it))
# # print(next(it))


# print(type(it))
# print(type(data))


# def name(n):
#     na = n
#     return na

# A = name("Rohit")

# print(A)

# def Print_Num():
#     yield 10
#     yield 20  
#     yield 30

# data = Print_Num()
# print(next(data))
# print(next(data))
# print(next(data))


# def print_data():
#     print("hello")
#     print_data()
    
# print_data()

# def factorial (n):
    
#     if n==1:
#         return 1
#     return n * factorial(n-1)

# data = factorial(11)
# print(data)


# def rev (n):
#     if n==1:
#         return 1
#     return n , rev(n-1)

# reve = rev(4)
# print(reve)

# data = (12, 3.6, 345, 3456, True,False, [2,3,"Rohit", True])
# print(data)
# print(type(data))

# data1 = (0,)
# print(data1)
# print(type(data1))

# print(data[len(data)-1])

# data [3:6]

# # data[4] = 43
# print(data)

# for datas in data: 
#     print(data)

data = {
    "Name": "Rohit",
    "Age": 20,
    "city": "Muzaffarpur",
    "isAlive" : False,
    
}

print(data)

print(data["isAlive"])
    





