#!/usr/bin/env python3
import pdb
def print_fibonacci(length):
    num_array = []
    for i in range(length):
        if i==0 or i==1:
            num_array.append(i)
        else:
            new_value = num_array[i-1]+num_array[i-2]
            num_array.append(new_value)
        
        # pdb.set_trace()
        # num_array.append(i)
    # pdb.set_trace()
    print(num_array)
    # return num_array
        
        