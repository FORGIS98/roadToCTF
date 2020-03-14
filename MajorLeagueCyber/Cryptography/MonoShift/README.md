# Mono Shift
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

## Solucion
Los ctf sulen tener un formato de respuesta tipo `flag{...}` con el texto que nos dan es fácil saber que `uapv` es la palabra `flag`. Con eso en mente, como `u` va a ser `f` el salto es de 11. Así que saltamos cada letra de 11 y tenemos el flag.
