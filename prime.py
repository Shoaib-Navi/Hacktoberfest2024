# Function to check if a number is prime
def is_prime(num):
    # 0 and 1 are not prime numbers
    if num <= 1:
        return False
    # Check from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input a number from user
num = int(input("Enter a number: "))

# Output result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
