#!/usr/bin/env python

# first.py --- my first python file

def fib(x):
    if x <= 2:
        return 1
    return fib(x-1) + fib(x-2)

def main():
    # put the main things here
    print( fib(10) )

if __name__ == "__main__":
    main()


