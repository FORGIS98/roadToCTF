# Vigenere
Si has logrado pasar el primer nivel, no debería ser complicado que descifres también este ;)  

Texto en la página de Atenea.  

# Solucion:
Paso 1: Como no tenemos ni idea de cual es la contraseña que se ha usado, vamos a coger un trozo del texto, en este caso el principio `qv ah pfsix xi wm ughgsm` y vamos a hacer suposiciones. `qv` y `ah` (suponiendo que el texto esta en castellano) podemos pensar que es `de un`, `en un`, `es la` etc...  
Paso 2: Pongamos que nos la jugamos a que es `en un` (en este caso, se que es `en un`). Que 4 primeras letras tiene la contraseña para que `qv ah` pase a ser `en un`? Pues las 4 primeras letras son `mi gu`.   
Paso 3: La buena fuerza bruta, dejando `mi gu` estatico, probamos como locos con `migua`, `migub`...`miguz`, `miguaa`, `miguab`...  
Paso 4: Olvidar lo pasos anteriores y buscar en google vigenere decode online o algo así, he aquí la web que yo use https://www.guballa.de/vigenere-solver. Copias el texto entero y esto lo descifra por ti. Y no te complicas.  
