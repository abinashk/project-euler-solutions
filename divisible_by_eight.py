'''
You are given an integer N. Is there a permutation of digits of integer that's divisible by 8?
A permutation of digits of integer N is defined as an integer formed by rearranging the digits of N.
For example, if the number N = 123, then {123, 132, 213, 231, 312, 321} are the possible permutations.
'''

import sys
import itertools

def is_divisible_by_eight(x):
    if len(x) == 1:
        perms = [x for x in itertools.permutations(x, r=1)]
    elif len(x) == 2:
        perms = [x for x in itertools.permutations(x, r=2)]
    elif len(x) >= 3:
        perms = [x for x in itertools.permutations(x, r=3)]
    else:
        perms = []
    res = any([x % 8 == 0 for x in [int(''.join(y)) for y in perms]])
    return res

if __name__ == '__main__':
  a = '123991823789071237928734897298378928379827398723819219281928172871827918729871298172981721982719827918729'
  print is_divisible_by_eight(a)
