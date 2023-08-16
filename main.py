import art

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

num1 = int(input("What's the first number?"))

for key in operations:
  print(key)
  
function = input("Which operation do you want to use?")
num2 = int(input("What's the second number?"))
calculate = operations[function]
answer = calculate(num1, num2)

print(f"{num1} {function} {num2} = {answer}")