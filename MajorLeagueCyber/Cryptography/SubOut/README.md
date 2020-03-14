# Sub Out
The substitution cipher is the kind of challenge that you'd find inside of a cereal box. The ones with the puzzles and the decoder rings.

Except it gets more complicated if you don't have the decoder ring!

## Solucion

Prueba y error amigos, cada letra corresponde con otra. Lo primero es buscar algo familiar, como muchos retos, la forma de presentar la solución es con `flag{...}` es fácil cazar eso en el texto. Con eso en mente tenemos que en la última linea `izu rpjm ky "flag"` equivale a `the flag is "flag"`. Asi que ya tenemos un par de letras por las que empezar, las `i` son `t` y así sucesivamente. El script funciona empezando con ambos abcedarios igual, y las letras de abajo se van cambiando según se averiguan nuevas.

