#DSC 510
#Week 5
#Programming Assignment Week 5
#Breanna Parker
#10/1/22


# The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
# Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
# This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
# This function will print the calculated value for the end user.
# Define a function named calculateAverage which takes no parameters.
# This function will ask the user how many numbers they wish to input.
# This function will use the number of times to run the program within a for loop in order to calculate the total and average.
# This function will print the calculated average.
# This program will have a main method which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
# The main method should prompt the user for the operation they wish to perform.
# The main method should evaluate the entered data using if statements.
# The main method should call the necessary function to perform the calculation.

def performCalculation (operation):
  num1 = float(input("What is your first number?\n"))
  num2 = float(input("What is your second number?\n"))
  if operation == "+":
    answer = num1 + num2
  elif operation == "-":
    answer = num1 - num2
  elif operation == "*":
    answer = num1*num2
  elif operation == "/":
    answer = num1 / num2    
  print (answer)
  
def calculateAverage():
  total = 0
  n = int(input("Enter number of numbers : "))
  arr = list(map(int,input("\nEnter the numbers for average : ").strip().split()))[:n]
  for a in arr:
    total = total + a
  answer = "{:.2f}".format(total / n)
  print(answer)


def main():
  while True:
    line = input ("Choose 1 or 2 or done\n")
    if line  == "1":
      n = input("Choose +, -, /, or * \n")
      performCalculation(n)
    elif line == "2":
      calculateAverage()
    elif line == 'done':
      break
    else:
      print("Error, pick 1, 2 or done")
  print("Done!")

main()
  
  