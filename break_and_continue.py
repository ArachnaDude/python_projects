
largest_number = -99999999
counter = 0


# Break variant

# while True:
#   number = int(input("Enter a number or type -1 to quit: "))
#   if number == -1:
#     break
#   counter += 1
#   if number > largest_number:
#     largest_number = number

# if counter != 0:
#   print("Largest number is: ", largest_number)
# else:
#   print("No number entered")



# Continue variant

# number = int(input("Enter a number or type -1 to quit: "))

# while number != -1:
#   if number == -1:
#     continue
#   counter += 1

#   if number > largest_number:
#     largest_number = number
#   number = int(input("Enter a number or type -1 to quit: "))

# if counter:
#   print("The largest number is: ", largest_number)
# else:
#   print("No number entered")



# secret_word = "chupacabra"

# while True:
#   user_word = input("Guess the secret word: ")
#   if user_word == secret_word:
#     break

# print("You've successfully left the loop")


user_word = input("Enter a word: ")
user_word =  user_word.upper()

disemvoweled_word = ""

for letter in user_word:
  if letter == "A":
    continue
  elif letter == "E":
    continue
  elif letter == "I":
    continue
  elif letter == "O":
    continue
  elif letter == "U":
    continue
  else: disemvoweled_word += letter

print(disemvoweled_word)

