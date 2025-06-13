def find_pairs(num_string):

  # 1: convert the string into a list of integer
  new_string = num_string.split(" ")
  num_list = []
  for string in new_string:
    num_list.append(int(string))
  

  if len(num_list) < 2:
    return set()
  # 2: initiate a set to store the results
  paring_set = set()

  # 3, for i in the list,
  for i in range(len(num_list)-1):
    for j in range(i+1, len(num_list)):
      if num_list[i] < num_list[j]:
        new_pair = (num_list[i], num_list[j])
        paring_set.add(new_pair)
      else: 
        new_pair = (num_list[j], num_list[i])
        paring_set.add(new_pair)

  return paring_set
  
      
  # 4, for j in the range (i, len(list))
  # 5, check if (i, j) is the result, i, j is in the right order, i < j
  # 6, return the set

  # Write your solution here!
 


# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")