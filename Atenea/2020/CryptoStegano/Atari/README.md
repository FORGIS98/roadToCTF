# Atari

binwalk Atari2600-614a2cd9d500901ea3944785b4d9b3ab.jpg
unzip -l Atari2600-614a2cd9d500901ea3944785b4d9b3ab.jpg
r2 -w Atari2600-614a2cd9d500901ea3944785b4d9b3ab.jpg
unzip Atari2600-614a2cd9d500901ea3944785b4d9b3ab.jpg
 r2 -w test.jpg
strings -t x test.jpg | grep A.gif
r2 -w test.jpg
binwalk Atari2600-614a2cd9d500901ea3944785b4d9b3ab.jpg
cp Atari2600-614a2cd9d500901ea3944785b4d9b3ab.jpg test.jpg
r2 -w test.jpg
binwalk test.jpg
unzip test.jpg
feh A.gif
exiftool A.gif
binwalk A.gif
dd if=A.gif bs=1 skip=1069586 of=B.gif
feh B.gif
dd if=A.gif bs=1 count=1069586 of=C.gif
feh C.gif

# Solucion

El archivo Atari... es el original.
El archivo AtariNoOriginal...es...obviamente...el que he modificado.

Paso 1: Reto interesante, lo primero es analizar la foto con `binwalk` el cual nos dice algo interesante. Encuentra el final de un archivo `Zip` pero...y el princicpio? Si ejecutamos `zunip -l` vemos que hay un archivo `A.gif`, osea que el zip no esta vacio.
Paso 2: Vamos a google, wikipedia, buscamos que `magic number` tienen los archivos `zip`. Vemos que hay 3 magic number, nos quedamos con 2 de ellos, uno es el basico, el otro es cuando el archivo esta vacio `50 4B 03 04` y `50 4B 05 06` lo que buscamos es ir al principio del zip y ver que `magic number` tiene y cambiarlo por el básico, para que se detecte como que hay un zip con contenido en vez de un zip vacio.
Paso 3: Lo que tenemos que hacer es buscar el principio del archivo zip. Para ello podemos imprimir todas las veces que aparece `A.gif` puesto  que sabemos que ese archivo tiene que estar dentro del zip. Para ello `strings -t x Atari... | grep A.gif`. Obtenemos que aparece en dos lugares, nos interesa el primero. Abrimos con `radare2 -w` la imagen y con el comando `s <posicion>` siendo posicion lo que os haya devuelto el comando `strings` (ponedlo con 0x delante) nos movemos a la posicion de memoria dada. Pulsamos V.
Paso 4: Tiramos hacia atras desde ese punto despacito buscando `PK` o `50 4B 05 06` una vez encontrado entramos con la `i` en modo inserción y cambiamos ese valor por `50 4B 03 04`.
Paso 5: Salimos de radare con `<ESC> q` y luego `q` otra vez y le dais al enter (mas o menos así se sale) y ya podemos hacer `unzip Atari...` y tenemos `A.gif`. Aqui le cambie el nombre a Atari... y le puse AtariNoOrignal.
Paso 6: Le he cambiado el nombre al gif, ahora se llama `father.gif`. Hacemos `binwalk` al `father.gif` y vaya, un gif dentro de un gif. Bien, vamos a separar ambos gif con `dd` no es la mejor forma pero nos saca del apuro. Con los datos que devuelve binwalk escritos en decimal hacemos: `dd if=father.gif bs=1 skip=1069586 of=brother.gif` con esto sacamos el segundo gif, y ahora saquemos al primero para tenerlos aislados, `dd if=father.gif bs=1 count=1069586 of=sister.gif`.
Paso 7:
