def prison_break(list):
  
  # invert function checks each element of passed list, appending the inverse to a new list. This list is the return value of invert()
  def invert(list_to_invert):
    new_list = []
    for i in list_to_invert:
      if i == 1:
        new_list.append(0)
      else:
        new_list.append(1)
    return new_list
  

  modded_prison = list
  prisoner_counter = 0

  # for loop iterates through modded_prison list, increments counter by 1, and calls invert() on prison list every time a 1 is encountered  
  for i in range(len(modded_prison)):
    if modded_prison[i] == 1:
      prisoner_counter += 1
      modded_prison = invert(modded_prison)


  # once loop is complete, prisoner_counter is returned  
  return prisoner_counter

# Test cases
prison0 = [0, 0, 0] # returns 0
prison1 = [1, 1, 1] # returns 1
prison4 = [1, 1, 0, 0, 0, 1, 0] # returns 4
prison6 = [1, 1, 0, 1, 0, 1, 0] # returns 6

print(prison_break(prison4))