"""Running the caclulator"""
from src.calculator import addIntegers, subtractIntegers

num1: int = 10
num2: int = 5

addResult: int = addIntegers(num1, num2)
subtractResult: int = subtractIntegers(num1, num2)

print(f"Adding {num1} and {num2} equals {addResult}")
print(f"Subtracting {num2} from {num1} equals {subtractResult}")
