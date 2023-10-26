#############
#Assignment 1
#############

############
#Question 1
############
print("QUESTION 1")

operation_a = 10*(90+2)-5
print("10*(90+2)-5 =", operation_a)

operation_b = 10*90+2-5
print("10*90+2-5 =", operation_b)

operation_c = 10*90+(2-5)
print("10*90+(2-5) =", operation_c)

operation_d = 10.0*(90+2)-5
print("10.0*(90+2)-5 =", operation_d)

operation_e = 120/(20+40)-(6-2)/4
print("120/(20+40)-(6-2)/4 =", operation_e)

operation_f = 5.0/2
print("5.0/2 =", operation_f)

operation_g = 5/2
print("5/2 =", operation_g)

operation_h = 5.0/2.0
print("5.0/2.0 =", operation_h)

operation_i = 5/2.0
print("5/2.0 =", operation_i)

operation_j = 678%3*(8-(9/4))
print("678%3*(8-(9/4)) =", operation_j)


############
#Question 2
############
print("QUESTION 2")

id = int(input("Enter your ID:"))
print("Your profile - ID:", "0" + str(id))

name = input("Enter your Name:")
name = name.upper().strip()
print("name:", name)

#DOB

address = input("Enter your Address:")
address = address.lower().strip()
print("Address:", address)


############
#Question 3
############
print("QUESTION 3")

number = input("Enter your number:")
print(number, "has", len(number), "digits")


############
#Question 4
############
print("QUESTION 4")

your_grade = eval(input("Enter your grade:"))
if your_grade >= 97:
  letter_grade = "A+"
elif your_grade < 97 and your_grade >= 93:
  letter_grade = "A"
elif your_grade < 93 and your_grade >= 90:
  letter_grade = "A-"
elif your_grade < 90 and your_grade >= 87:
  letter_grade = "B+"
elif your_grade < 87 and your_grade >= 83:
  letter_grade = "B"
elif your_grade < 83 and your_grade >= 80:
  letter_grade = "B-"
elif your_grade < 80 and your_grade >= 77:
  letter_grade = "C+"
elif your_grade < 77 and your_grade >= 73:
  letter_grade = "C"
elif your_grade < 73 and your_grade >= 70:
  letter_grade = "C-"
elif your_grade < 70 and your_grade >= 67:
  letter_grade = "D+"
elif your_grade < 67 and your_grade >= 63:
  letter_grade = "D"
elif your_grade < 63 and your_grade >= 60:
  letter_grade = "D-"
else: 
  letter_grade = "F"

print(your_grade, "is equivalent to a", letter_grade)

############
#Question 5
############
print("QUESTION 5")

pattern = []

number = int(input("Enter your number:"))
for i in range(number):
  pattern.append("*")
  print(pattern)

reverse = len(pattern)
for x in range(reverse):
  pattern.remove("*")
  print(pattern)

############
#Question 6
############
print("QUESTION 6")

lower = int(input("Enter the lower number:"))
higher = int(input("Enter the higher number:"))

while lower > higher: 
  print("Please try again")
  lower = int(input("Enter the lower number first:"))
  higher = int(input("Enter the higher number second:"))

#Then while lower < higher and for lower%2 == 0 print lower. After the first try we add 1 to the lower number and try again, up until reaching the higher number. 
