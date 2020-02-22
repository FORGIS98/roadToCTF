# Exclusor
The Exclusive-Or (XOR) operation is a basic primitive of cryptography. Because the XOR of two values can be XOR'ed again with one of the original operands to get the other operand, it's been used to implement basic encryption schemes.

We encrypted this flag using the XOR Cipher but we'll give you the key.

# Solution
So XOR gates work like this:
```
| INPUT | OUTPUT  |
|---|---|----|----|
| A | B | A XOR B |
| 0 | 0 |    0    |
| 0 | 1 |    1    |
| 1 | 0 |    1    |
| 1 | 1 |    0    |
```
Knowing that, 0 ^ 0 = 0 and so on, so by doing the XOR of each character on the flag with each character on the key we can XOR'ed the data back. And that's what python script does.
