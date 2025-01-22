numbers = ["zero", "one", "two", "three", "four", "five", 
          "six", "seven", "eight", "nine", "ten", 
          "eleven", "twelve", "thirteen", "fourteen", 
          "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

number = int(input("Enter a number (0-19): "))

if 0 <= number <= 19:
  print(f"The number{number} is: {numbers[number]}") 
else:
  print("Invalid input.") 