# coding: utf-8

from prng.random_number_generator import *


class RandomLinearShiftRegister(RandomNumbersGenerator):

    def __init__(self, bits_count, bits_to_xor):
        super().__init__()
        self.name = "Random Linear Shift Register Generator"
        self.bits_to_xor = bits_to_xor
        self.mask = 2**bits_count-1
        self.seed &= self.mask

        print(format(self.seed, "0b"))

    def __str__(self):
        result = "Bn = "

        for bit in self.bits_to_xor[:-1]:
            result += "Bn-{} ^ ".format(bit)

        result += "Bn-{}".format(self.bits_to_xor[-1])

        return result

    def rand(self):
        new_bit = (self.seed >> self.bits_to_xor[0]) & 1

        for bit in self.bits_to_xor[1:]:
            new_bit ^= (self.seed >> bit) & 1

        self.seed <<= 1  # Will create an integer n+1 bits long
        self.seed += new_bit  # Change the new LSB value
        self.seed &= self.mask  # Remove the MSB to have an integer which is n bits long

        result = 0

        for i in range(self.seed.bit_length()):
            current_bit = (self.seed >> i) & 1
            result += 2**i * current_bit

        return result / (2**8)

