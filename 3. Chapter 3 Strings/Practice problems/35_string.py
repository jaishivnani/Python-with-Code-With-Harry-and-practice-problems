'''Hackerank Problem 3 What's Your Name?'''
# Sample Output:- Hello Ross Taylor! You just delved into python."


def print_full_name(a, b):
    print(f"Hello {a} {b}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)




