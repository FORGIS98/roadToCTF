# Mono Shift
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

## Solution
We have this text `uapv{ndj'kt_qtvjc_ndjg_rgneid_psktcijgth}` ctf solutions sometimes comes with the format `flag{...}` and so is this one. They tell us that this is Caesar Cipher. So we have next logic: 
```bash
uapv{ndj'kt_qtvjc_ndjg_rgneid_psktcijgth}
flag{...}
```
so `u` is going to change to `f`, and `a` to `l`. That's a jump of 11 letters. So we just have to jump every letter by 11. That's what the little python script does.
