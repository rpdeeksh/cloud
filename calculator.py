# calculator.py

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: float, b: float) -> float:
    """Divide two numbers with error handling for division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a: float, b: float) -> float:
    """Calculate a raised to the power of b."""
    return a ** b

if __name__ == "__main__":
    print("=== Calculator Demo ===")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("3 * 4 =", multiply(3, 4))
    print("10 / 2 =", divide(10, 2))
    print("2 ^ 3 =", power(2, 3))
    
    # Test error handling
    try:
        print("10 / 0 =", divide(10, 0))
    except ValueError as e:
        print(f"Error: {e}")
