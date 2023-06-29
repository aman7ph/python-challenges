from art_and_data import day10challenge_Art
logo=day10challenge_Art.logo
print(logo)

coose1=True
while coose1:
    num1=float(input("What's the first number ?:\t"))
    print("+\n-\n*\n/")
    oprator=input("Pick an operation:\t")
    num2=float(input("What's the next number ?:\t"))
    coose2=True
    while coose2:
        if oprator=='+':
            result=num1+num2
            print(f"{num1} {oprator} {num2} = {result}")      
        elif oprator=='-':
            result=num1+num2 
            print(f"{num1} {oprator} {num2} = {result}")         
        elif oprator=='*':
            result=num1+num2 
            print(f"{num1} {oprator} {num2} = {result}")      
        elif oprator=='/':
            result=num1+num2 
            print(f"{num1} {oprator} {num2} = {result}")        
        choose=input("Type 'y' to continue calculating with 4.0,type 'n' to start a new calculation or type 'x' to exit:")
        if choose=='y':
            num1=result
            print("+\n-\n*\n/")
            oprator=input("Pick an operation:\t")
            num2=float(input("What's the next number ?:\t")) 
            coose2=True       
        elif choose=='n':
            coose2=False
        elif choose=='x':
            coose2=False
            coose1=False 
            print("GoodBy")
    



""" 
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator() """













































