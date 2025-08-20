# Calculator Application

A simple Python calculator application with Docker support and comprehensive testing.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Power operation
- Error handling for division by zero
- Comprehensive unit tests
- Docker containerization

## Local Development

### Prerequisites
- Python 3.10+
- pip

### Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the calculator:
```bash
python calculator.py
```

3. Run tests:
```bash
pytest test_calculator.py -v
```

## Docker Usage

### Build the Docker image:
```bash
docker build -t calculator-app .
```

### Run the container:
```bash
docker run calculator-app
```

### Run tests in container:
```bash
docker run calculator-app python -m pytest test_calculator.py -v
```

### Run interactive shell:
```bash
docker run -it calculator-app /bin/bash
```

## API Reference

### Functions

- `add(a: int, b: int) -> int`: Add two integers
- `subtract(a: int, b: int) -> int`: Subtract two integers  
- `multiply(a: int, b: int) -> int`: Multiply two integers
- `divide(a: float, b: float) -> float`: Divide two floats (raises ValueError for division by zero)
- `power(a: float, b: float) -> float`: Calculate a raised to the power of b

## Testing

The project includes comprehensive unit tests covering:
- All mathematical operations
- Error handling scenarios
- Edge cases

Run tests with:
```bash
pytest test_calculator.py -v
```
