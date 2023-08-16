import art
import os

clear = lambda: os.system('cls')

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = int(input("What's the first number? \n"))
  calculate_more = True

  while calculate_more:
    for key in operations:
      print(key)
    function = input("Which operation do you want to use? \n")
    num2 = int(input("Enter a number \n"))
    calculate = operations[function]
    answer = calculate(num1, num2)
    print(f"{num1} {function} {num2} = {answer}")
    num1 = answer
    again = input(f"Type 'y' to continue calculating with {answer} or type 'n to exit \n")
    if again.lower() == 'n':
      calculate_more = False
      clear()
      calculator()

calculator()