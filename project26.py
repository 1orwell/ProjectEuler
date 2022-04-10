from decimal import *
import math

# denominator will never change
# numerator will be the new remainder each time
# append to answer every time you know how many multiple of numerator fit into denominator

# Learned something new! The below line causing issues due to "mutable default values"
# def long_div(answer, numer, denom, check = []):

def long_div(answer, numer, denom, check):
    # if numerator is smaller than denominator, move to next column
    if numer < denom:
        answer.append(0) 
        return long_div(answer, numer*10, denom, check)
    else:
        # don't want to 'round' as that could round up, e.g. saying that 7 goes into 60 
        # 9 times instead of 8
        multiple = math.floor(numer/denom)
        answer.append(multiple)
        new_numer = (numer % denom) * 10
        if new_numer in check:
            return answer
        elif new_numer == 0:
            return answer
        else:
            check.append(new_numer)
            return long_div(answer, new_numer, denom, check)

dec_map = {}
tmp = [] 
index = 0

for i in range(1,1000):
    rep_lst = long_div([], 1, i, [])
    #print(f'1/{i} is {rep_lst}')
    if len(rep_lst) > len(tmp):
        tmp = rep_lst
        index = i
        dec_map[i] = rep_lst

print(f'tmp is {tmp}')
print(f'dec_map is {dec_map}')
print(f'index is {index}')
print(f'Final answer is {dec_map[index]}')


        

