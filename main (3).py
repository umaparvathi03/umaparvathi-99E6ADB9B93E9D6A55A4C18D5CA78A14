

"""
year%4==0&
year%100!=0/
year%400==0 

"""
def Leapyear (year):
 return bool (year%4==0and year% 100!=0or year%400==0)

year=int(input("Enter a year:"))

if Leapyear (year):
 print("{} is a leap year.".format(year))
 else:
print("{} is not a leap year. ".format(year))