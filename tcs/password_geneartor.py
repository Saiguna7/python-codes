import math
def convert_to_scientific_notation(number):

    mantissa, exponent = math.frexp(number)
    mantissa = int(str(mantissa)[2:])
    exponent = int(exponent)
    
    # Simplify digits
    while len(str(mantissa)) > 1:
        total = sum([int(digit) for digit in str(mantissa)])
        mantissa = total % 10
    
    while len(str(exponent)) > 1:
        exponent = sum([int(digit) for digit in str(exponent)]) % 10
    
    return f"{mantissa}.{mantissa}e{exponent}"

def generate_password(number, name):

    if not name.islower():
        return "Invalid"
    
    scientific_notation = convert_to_scientific_notation(number)
    S1 = "".join(word[:3] for word in scientific_notation.split())
    S2 = ""
    
    if int(scientific_notation[-1]) % 2 == 1:
        S2 = "".join([name[i] for i in range(1, len(name), 2)])
    
    return f"{S1}@{S2}"

def main():
    # Read number of test cases
    t = int(input())
    
    for _ in range(t):
        # Read number and name
        number, name = input().split()
        
        # Try converting to float
        try:
            number = float(number)
        except ValueError:
            print("Invalid")
            continue
        
        # Generate password and print
        password = generate_password(number, name)
        print(password)
