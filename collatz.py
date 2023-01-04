# Take any non-negative, non-zero int - c0
# if even, c0 = c0/2
# if odd, c0 = 3 * c0 + 1
# if c0 != 1, go back to step 2

c0 = int(input("Enter a non-zero, non-negative number: "))

steps = 0

while c0 != 1:
  if c0 % 2 == 0:
    c0 = c0//2
    print(c0)
    steps += 1
  else:
    c0 = 3 * c0 + 1
    print(c0)
    steps +=1

print("Steps: ", steps)