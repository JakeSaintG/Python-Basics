# Type hints
amount: int = 10
tax: float = .06
name: str = "jake"

# It doesn't seem to enforce var typing by default...
tax = "test"

# Casting/Converting
convertInt: int = 2319
convertFloat: float = 1.21 #gigawatts

print(float(convertInt))
print(int(convertFloat))

print(amount + amount)

print(tax + name)

#Will throw an error
print(tax + amount)