'''Hackerank Problem 1 sWAP cASE You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.'''
'''Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2'''

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)




