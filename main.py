#!/usr/bin/python3
# coding: utf8

from prng.random_linear_modulus import *
from prng.random_linear_shift_register import *


if __name__ == "__main__":
    r = RandomLinearModulus(6, 2, 24)
    r.seed = 5
    r.benchmark()

    r = RandomLinearModulus(3, 6, 2)
    r.seed = 5
    r.benchmark()

    r = RandomLinearShiftRegister(8, [3, 5, 8])
    r.benchmark()
