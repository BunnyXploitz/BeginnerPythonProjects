#Q1: Calculate 3% discount on the amount entered by the user and display the output as:
#The discount on <<amount>> is <<amount after discount>>

#Solution_Q1:
amt = int(input("Enter the amount: "))
dis = amt/100*3
amt_dis = amt-dis
print("The Discount on", amt, "is", amt_dis)


#Q2: Ganesh has a grassland on his farm house in a perfect circular shape. Accept circumference of the grassland and calculate its area. Circumference is double of radius and area of circle is calculated as 3.14*radius*radius

#Solution_Q2:
circumference = float(input("Enter the circumference of the grassland: "))
radius = circumference/2 #radius is half of the circumference
area = 3.14 * radius * radius
print("The area of the grassland is", area)


#Q3: Accept the height of the user in feet and inches separated by decimal. Example: 60.7 means 5 feet 7 inches. Then display the height in feet and inches separately. Example: Feet=5, Inches=7.0

#Solution_Q3:
height = input("Enter your height in feet and inches separated by decimal: ")
feet, inches = map(int, height.split("."))
print( "Feet:", feet/12, "\nInches:", inches)


#Q4: Display the Fibonacci series 1,1,2,3,5,8,13,21

#Solution_Q4:
# Get the number of terms from the user
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
a = 0
b = 1

# Print the first two terms (optional)
print(a, end=" ")
print(b, end=" ")

# Calculate and print the remaining terms
for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c


#Q5: Accept a 4-digit number and display it in reverse 

#Solution_Q5:
num = int(input("Enter a 4-digit number: "))
reversed_num = str(num)[::-1]
print("Reversed number:", reversed_num)


#Q6: Accept marks of 10 students in English and Hindi then count how many students have secured average marks of the two subjects as more than 60%

#Solution_Q6:
average = 0
count = 0
for i in range(1,11):
    hindi = int(input(f"Enter marks for student  {i} in Hindi: "))
    print(hindi)
    english = int(input(f"Enter marks for student  {i} in English: "))
    print(english)
    average = (hindi + english) / 2
    print("Average marks for student", i, "is", average)
    if average > 60:
        count += 1
    elif average < 60:
        count += 0
print("Number of Students who have scored more than 60% is",count)


#Q7: Write a Python Program to enter Your Basic Salary, HRA and DA. Then Calculate The Gross Salary and apply tax. If Gross Salary: 10-15LPA - 20% Tax, 15-20LPA - 25% Tax, Above 20LPA - 30% Tax


#Solution_Q7:
b_sal = int(input('Enter Your Basic Salary:  '))
hra = int(input('Enter Your HRA:  '))
da = int(input('Enter Your DA:  '))

g_sal = b_sal + hra + da 
if g_sal >= 1000000 and g_sal <= 1500000:
  tax = (g_sal/100) * 20
  print(f'Your Tax is of amount: {tax}')
elif g_sal >= 1500000 and g_sal <= 2000000:
  tax = (g_sal/100) * 25
  print(f"Your Tax is of amount: {tax}")
elif g_sal >= 2000000:
  tax = (g_sal/100) * 30
  print(f'Your Tax is of amount: {tax}')
else:
  print('Enjoy! No Tax')  