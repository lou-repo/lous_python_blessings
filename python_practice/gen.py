#!/usr/bin/python3

def gen_range(stop, start=1, step=1):
    num = start 
    while num <= stop:
        yield num
        num += step

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
