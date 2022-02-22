from random import randint


Stack = {}

def randomChoice():
        return randint(2, 15)

def holdInfoInStack(name: str,age: int,country: str , option: int):
 Stack[name.lower()] = [name,age,country,option]

def divider(n=20):
 print('-'*n)

def displayinfo(name: str,age: int,country: str)->tuple:
 holdInfoInStack (name,age,country,1)
 return name,age,country

def displayinfoByInput(name: str,age: int,country: str)->tuple:
 holdInfoInStack (name,age,country,2)
 return displayinfo(name,age,country)


if name == '__main__':
 name = "ESMT"
 age =30
 country = "senegal"
 divider()
 print(displayinfo(name,age,country))
 name2 = input(" Enter a name :")
 age2 =int(input(" Enter a age "))
 country2 = input("  Enter a country ")
 divider()
 print(displayinfoByInput(name2,age2,country2))