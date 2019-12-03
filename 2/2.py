# %% PART 1

import pandas as pd
import math

test = "1,1,1,4,99,5,6,0,99"
string = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,6,19,23,1,23,5,27,1,27,13,31,2,6,31,35,1,5,35,39,1,39,10,43,2,6,43,47,1,47,5,51,1,51,9,55,2,55,6,59,1,59,10,63,2,63,9,67,1,67,5,71,1,71,5,75,2,75,6,79,1,5,79,83,1,10,83,87,2,13,87,91,1,10,91,95,2,13,95,99,1,99,9,103,1,5,103,107,1,107,10,111,1,111,5,115,1,115,6,119,1,119,10,123,1,123,10,127,2,127,13,131,1,13,131,135,1,135,10,139,2,139,6,143,1,143,9,147,2,147,6,151,1,5,151,155,1,9,155,159,2,159,6,163,1,163,2,167,1,10,167,0,99,2,14,0,0"
orig_lst = [int(n) for n in string.split(',')]

def calculate(lst):
    for l in range(0,len(lst),4):
        current = lst[l]
        if current == 99:
            break
        else:
            next_1_number_pos = lst[l+1]
            next_2_number_pos = lst[l+2]
            next_3_number_pos = lst[l+3]
            
            next_1_number = lst[next_1_number_pos]
            next_2_number = lst[next_2_number_pos]
            
            if current == 1:
                addition = next_1_number + next_2_number
            elif current == 2:
                addition = next_1_number * next_2_number
            else:
                raise ValueError("Encoutering a value different than 1,2,99 should not be possible. Found value is: {}".format(current))
            lst[next_3_number_pos] = addition
    return lst

print(calculate(orig_lst.copy()))

# %% PART 2

print(orig_lst)

for i in range(0,100):
    for j in range(0,100):
        lst = orig_lst.copy()
        lst[1] = i
        lst[2] = j
        returned_list = calculate(lst)
        if returned_list[0] == 19690720:
            print("For the verb:{} and noun:{} the result is 19690720".format(i,j))
            print("Therefore the result = {}".format(100*i+j))
            break


# %%
