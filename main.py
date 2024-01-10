from itertools import combinations

howmuch_lst = [2,4,6,8]
howmany_lst = [2]
repeat = 1

for howmuch in howmuch_lst:
  print("for",howmuch)
  for howmany in howmany_lst:
    # Generate all combinations of 4 numbers from 1 through 9
    numbers = list(range(-9, 10))
    for i in range(1,repeat):
      numbers += list(range(1, 10))
    combinations_list = list(combinations(numbers, howmany))
    
    # Filter combinations that sum to 30 and don't have repeating digits
    result = [list(combo) for combo in combinations_list if sum(combo) == howmuch]
    # Print the result
    for combo in set(tuple(sorted(x)) for x in result):
        print(combo)