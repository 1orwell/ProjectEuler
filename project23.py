#success

import sympy
import itertools

def factors(num):
    factors_list = []
    if sympy.isprime(num):
        return [1]
    else:
        for val in range(1, num):
            if num % val == 0:
                factors_list.append(val)
        return factors_list

def abundant(max):
    abundant_lst = []
    for val in range(max):
        factor_list = factors(val)
        sum_factors = sum(factor_list)
        if sum_factors > val:
            abundant_lst.append(val)
    # list of all possible abundant numbers below given max
    return abundant_lst

def summing_lst(lst):
    combo_lst = []
    bool_dict = {}
    total = 0
    # creating list of all combinations of 2 possible abundant numbers in given list
    for num in lst:
        tup = (num, num)
        combo_lst.append(tup)
    for subset in itertools.combinations(lst, 2):
        combo_lst.append(subset)
    # summing all possible combos together
    for combo in combo_lst:
        bool_dict[sum(combo)] = True
    for i in range(28125):
        # using dict instead of list for quicker lookup
        if i not in bool_dict:
            total += i
            print(f'Adding {i} to total, new total is {total}')
    print(total)

# choosing number well over max number than can be found by summing two abundant numbers together
# making sure don't miss any
abundant_lst = abundant(30000)
summing_lst(abundant_lst)