from typing import Union


def calculate(operator: str, num1: float, num2: float) -> Union[float, str]:
   """
   Performs basic arithmetic operations on two numbers.

   Args:
       operator: The arithmetic operator (+, -, *, /).
       num1: The first number.
       num2: The second number.

   Returns:
       The result of the operation, or an error message if the operator is invalid.
   """

   if operator == "+":
       result = num1 + num2
   elif operator == "-":
       result = num1 - num2
   elif operator == "*":
       result = num1 * num2
   elif operator == "/":
       if num2 == 0:
           return "Division by zero is not allowed"
       result = num1 / num2
   else:
       return f"{operator} is not a valid operator"

   return round(result, 3)

# Example usage
result = calculate("+", 5.2, 3.1)
print(result)  # Output: 8.3

result = calculate("-", 10, 4)
print(result)  # Output: 6.0

result = calculate("*", 2, 5)
print(result)  # Output: 10.0

result = calculate("/", 12, 3)
print(result)  # Output: 4.0

result = calculate("/", 10, 0)
print(result)  # Output: Division by zero is not allowed

result = calculate("%", 10, 3)
print(result)  # Output: % is not a valid operator