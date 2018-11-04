# Pseudo Random Numbers Generators
PRNGs implementations in Python 3. This repository is for educational purpose only, it's not cryptographically secure. Use well known and certified PRNG libraries to avoid mistakes.

## Random Linear Modulus

### Function 1
```
Values sample :  [32, 194, 1166, 6998, 41990, 251942, 1511654, 9069926, 4087910, 7750246]
Benchmarking Random Linear Modulus Generator...
f(k) = 6 x k + 2 (mod 2^24)
Found period :  14
Done in 1.20 seconds.
```

![alt prng1_1](https://github.com/ShellCode33/PseudoRandomNumbersGenerators/raw/master/screenshots/prng1_1.png)
![alt prng1_2](https://github.com/ShellCode33/PseudoRandomNumbersGenerators/raw/master/screenshots/prng1_2.png)

### Function 2
```
Values sample :  [21, 69, 213, 645, 1941, 5829, 17493, 52485, 157461, 472389]
Benchmarking Random Linear Modulus Generator...
f(k) = 3 x k + 6 (mod 2^24)
Found period :  524288
Done in 1.47 seconds.
```

![alt prng2_1](https://github.com/ShellCode33/PseudoRandomNumbersGenerators/raw/master/screenshots/prng2_1.png)
![alt prng2_2](https://github.com/ShellCode33/PseudoRandomNumbersGenerators/raw/master/screenshots/prng2_2.png)

## Random Linear Shift Register
```
Values sample :  [0.203125, 0.41015625, 0.8203125, 0.640625, 0.28515625, 0.57421875, 0.1484375, 0.30078125, 0.6015625, 0.203125]
Benchmarking Random Linear Shift Register Generator...
Bn = Bn-0 ^ Bn-1 ^ Bn-2 ^ Bn-3 ^ Bn-4 ^ Bn-5 ^ Bn-6 ^ Bn-7
Found period :  9
Done in 6.01 seconds.
```

![alt prng3_1](https://github.com/ShellCode33/PseudoRandomNumbersGenerators/raw/master/screenshots/prng3_1.png)
![alt prng3_1](https://github.com/ShellCode33/PseudoRandomNumbersGenerators/raw/master/screenshots/prng3_2.png)
