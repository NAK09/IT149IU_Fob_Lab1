n = int(input("Enter a three-digit integer: "))

hundreds = n // 100
tens = (n // 10) % 10
units = n % 10

digit_sum = hundreds + tens + units

reversed_num = units * 100 + tens * 10 + hundreds

is_palindrome = (n == reversed_num)

print(f"Hundreds digit: {hundreds}")
print(f"Tens digit: {tens}")
print(f"Units digit: {units}")
print(f"Sum of digits: {digit_sum}")
print(f"Reversed number: {reversed_num}")

if is_palindrome:
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")