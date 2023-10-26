print("Question 1")

def reverseString(s,i):
  if i == 0: 
    return ""
  return s[::-1]*i 
  
###Didn't know how to concatenate.
#If the user enters 0 for the number of repetitions, the code will return an empty string.
#Else, the code will create a slice that will start at the end of the string and end at the start of it, moving one step backwards. 
  
phrase = input("Please enter your phrase here: ")
repetition = int(input("Please enter the number of repetitions: "))

while repetition < 0:
  print("Invalid, please enter a positive number.")
  repetition = int(input("Please enter the number of repetitions: "))

#If the user enters a negative number, the code will state that it's an invalid input and asks for input agian.

print("The reverse of", phrase, repetition, "times in a row is:", reverseString(phrase, repetition))
#Lastly, the function is called, with both phrase and repetition, passed as parameters.

print("")
print("")

print("Question 2")

def rearrangeLetters(s): 
  upper = ""
  lower = ""
#Two empty strings are created, one for the lowercase characters, and the other for the uppercase ones. 
  for i in s:
    if i.isupper():
      upper += i
    else:
      lower += i
  return upper + lower
#This checks every character in string s, then evaluates if it's uppercase or lowercase, then adds it to the respective string. Finally it returns both upper and lower strings. 
phrase2 = input("Please enter you phrase here: ")
print(rearrangeLetters(phrase2))

print("")
print("")

print("Question 3")

def checkElements(s1,s2):
  if set(s1) == set(s2):
    return True
  return False

#First, the function converts both parameters into sets to check characters of both s1 and s2. Then it will return true if elements of s1 are the same as the elements in s2. 

element1 = input("Please enter your first element: ")
element2 = input("Please enter your second element: ")
print(checkElements(element1, element2))

#The function is called in this print statetment to execute the code. 

print("")
print("")

print("Question 4")
# def getMax(l):
#   for i in l:
#     if i+1 > i:
#       maximum = l[i+1]
#     else: 
#       maximum = l[i]

# number = int(input("Enter how many numbers do you have: "))
# for x in range(number):
#   list = int(input("Enter your number here: "))
  
# print(getMax(list))

print("")
print("")

print("Question 5")

def calculateDigitsSum(n):
  if n == 0:
    return 0
  return n%10 + calculateDigitsSum(n//10)
#If n is different than 0, the code returns n%10 (which is the last digit of n), then calls the function to 

number1 = int(input("Enter your number here: "))
print(calculateDigitsSum(number1))

print("")
print("")

print("Question 6")

def removeDuplicates(s):
  if len(s) == 0 or len(s) == 1:
    return s
  if s[0] == s[1]:
    return removeDuplicates(s[1])
  else:
    return s[0] + removeDuplicates(s[1]) 
#Whenever we have an empty string, or with only one character it'll return the string itself. Otherwise, when two consecutive characters are the same the removeDuplicates function is called, whereas if they're not the same it'll print the first character then enters the function again for the following character
string = input("Enter your phrase here: ")
print(removeDuplicates(string))


print("")
print("")

print("Question 7")

#Let's say our result will be 4321, it is 4*1000 + 3*100 + 2*10 + 1
#To get that in a recursion, it should be n%10 (The last digit) * 10^(number of digits-1)
def getReverse(n):
  if n == 0:
    return 0
  return (n%10 + getReverse((n-1)//10)*10)

number2 = int(input("Enter your number here: "))
print(getReverse(number2))