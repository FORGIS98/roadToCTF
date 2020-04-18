# White Pages
I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

# Solucion
Dentro hay espacios cortos y largos, podemos pensar que es morse o binario, primero probe con python a imprimir los valores en unicode o ascii con la función `ord()` y vi que teniamos el `32` que es un espacio y el `8195` que en unicode es `u\2003`. El caso es que probe con binario, el 32 será un 1 y el 8195 un 0.

res:
		picoCTF

		SEE PUBLIC RECORDS & BACKGROUND REPORT
		5000 Forbes Ave, Pittsburgh, PA 15213
		picoCTF{not_all_spaces_are_created_equal_0696a7c2dfa36b081b44603b8aa78efd}

