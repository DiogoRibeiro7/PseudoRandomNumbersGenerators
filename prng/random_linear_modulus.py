# coding: utf-8

from prng.random_number_generator import *

class RandomLinearModulus(RandomNumbersGenerator):

    def __init__(self, a, b, m):
        super().__init__()
        self.name = "Random Linear Modulus Generator"
        self.a = a
        self.b = b
        self.m = m
        self.seed %= 2**m  # seed modulus 2**m

    def __str__(self):
        return "f(k) = {} x k + {} (mod 2^{})".format(self.a, self.b, self.m)

    def rand(self):
        self.seed = (self.a * self.seed + self.b) % (2**self.m)
        return self.seed

