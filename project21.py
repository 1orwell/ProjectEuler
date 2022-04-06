import sympy

amic_dict = {}
amic_list = []

def factors(num):
    factors_list = []
    if sympy.isprime(num):
        return [1]
    else:
        for val in range(1, num):
            if num % val == 0:
                factors_list.append(val)
        return factors_list

for i in range(1, 10000):
    print(i)
    factors_list = factors(i)
    sum_factors = sum(factors_list)
    amic_dict.setdefault(i, sum_factors)
    #print(f'The sum of the factors of {i} are {sum_factors}')
    if sum_factors in amic_dict:
        #print(f'The sum of the factors of {i} already exists in the list')
        if i == amic_dict[sum_factors] and amic_dict[i] != amic_dict[sum_factors]:
            #print(f'The value of {i} is {amic_dict[i]}')
            #print(f'The value of {sum_factors} is {amic_dict[sum_factors]}')
            amic_list.append(i)
            amic_list.append(sum_factors)

print(amic_list)
print(sum(amic_list))


