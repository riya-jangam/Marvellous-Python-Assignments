
num = int(input("Enter a number: "))

digit_sum = 0

while num > 0:
    digit = num % 10        # Get the last digit
    digit_sum += digit      # Add it to the sum
    num = num // 10         # Remove the last digit
    
# Output the result
print("Sum of digits is:", digit_sum)
