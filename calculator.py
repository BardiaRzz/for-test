def add(x, y):
  """Returns the sum of x and y."""
  return x + y

def subtract(x, y):
  """Returns the difference of x and y."""
  return x - y

def multiply(x, y):
  """Returns the product of x and y."""
  return x * y

def divide(x, y):
  """Returns the division of x by y."""
  if y == 0:
    raise ValueError("Error: Cannot divide by zero.")
  return x / y

def main():
  """Main function to run the calculator."""
  print("Welcome to the simple calculator!")
  print("Available operations:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")

  while True:
    choice = input("Enter your choice of operation (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
      print("Invalid operation choice. Please select a valid operation.")
      continue

    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
    except ValueError:
      print("Invalid input. Please enter numeric values.")
      continue

    try:
      if choice == '1':
        result = add(num1, num2)
      elif choice == '2':
        result = subtract(num1, num2)
      elif choice == '3':
        result = multiply(num1, num2)
      elif choice == '4':
        result = divide(num1, num2)

      print(f"The result is: {result}")

    except ValueError as e:
      print(e)
      continue

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
      break

if __name__ == "__main__":
  main()
