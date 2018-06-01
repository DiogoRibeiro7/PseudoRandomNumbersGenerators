#!/usr/bin/python3
# coding: utf8

from prng.random_linear_modulus import *
from prng.random_linear_shift_register import *


if __name__ == "__main__":
    r = RandomLinearModulus(6, 2, 24)
    r.seed = 5
    print("Values sample : ", [r.rand() for i in range(10)])
    r.benchmark()

    r = RandomLinearModulus(3, 6, 24) # m = 1 <=> modulus = 2^1 = 2
    r.seed = 5
    print("Values sample : ", [r.rand() for i in range(10)])
    r.benchmark()

    r = RandomLinearShiftRegister(8, [0, 1, 2, 3, 4, 5, 6, 7])
    print("Values sample : ", [r.rand() for i in range(10)])
    r.benchmark()
