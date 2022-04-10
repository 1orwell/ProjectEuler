from decimal import *

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
        multiple = round(numer/denom)
        answer.append(multiple)
        new_numer = (numer % denom) * 10
        if new_numer in check:
            return answer
        elif new_numer == 0:
            return answer
        else:
            check.append(new_numer)
            return long_div(answer, new_numer, denom, check)

print(long_div([], 1, 7, []))

for i in range(1,10):
    rep_lst = long_div([], 1, i, [])
    print(f'1/{i} is {rep_lst}')
