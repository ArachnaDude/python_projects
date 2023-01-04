blocks = int(input("Enter number of blocks: "))

# Takes a number of blocks - n

# rows starts at 1, height counter starts at 1

# add 1 to number, each turn of the loop increases height counter by 1

# if rows < number, keep going,

height = 0
blocks_left = blocks
blocks_in_next_row = 1

while blocks_left > 0:
  if blocks_left < blocks_in_next_row:
    break
  blocks_left -= blocks_in_next_row
  blocks_in_next_row += 1
  height += 1

print(blocks_left)
print(blocks_in_next_row)
print("Pyramid height: ", height)