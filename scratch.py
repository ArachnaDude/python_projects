# take initial int to start program
number = int(input("Enter a number, or -1 to end program: "))

entered_numbers = []

while number != -1:
  # store entered numbers in list
  entered_numbers.append(number)
  
  number = int(input("Enter a number, or -1 to end program: "))

# calculate total value of list, and divide it by the length of the list, to calculate average
total = sum(entered_numbers)
average = total/len(entered_numbers)
print(average)
