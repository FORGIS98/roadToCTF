# Retos Basicos
Dados los pocos pasos a seguir para resolver los retos básicos, hago un simple resumen que los engloba a todos.  

Además no incluyo los archivos de las pruebas.  

## Retos Hash, Hash2 y Hash3
Hash 1: Nos dan `LearnTheHashFunction`, ejecutamos en la terminal `echo -n "LearnTheHashFunction" | md5sum`.  

Hash 2: Nos dan `ThisIsAMoreSecureHashFunction`, ejecutamos en la terminal `echo -n "ThisIsAMoreSecureHashFunction" | sha256sum` lo que devuelve `d191ce0a9d8061acb609be613d0a6dccd13d93946fa3e8aa3c0c40a2102502ff`. Y ejecutamos `echo -n "d191ce0a9d8061acb609be613d0a6dccd13d93946fa3e8aa3c0c40a2102502ff" | md5sum`.  

Hash 3: Nos dan `54f662a095fa3d5fbbdaac72d176701b`, haciendo uso de una página web como: https://crackstation.net/ sacamos el euivalente en texto. Y ejecutamos `echo -n "MASTEROFPUPPETS" | md5sum`.  

## Retos ASCII, Base64 y Hexadecimal
ASCII: Buscamos en google `ASCII to text` y hacemos lo del `hash`.  

Base64: Buscamos en google `base64 to text` y hacemos lo del `hash`.  

Hexadecimal: Adivina...buscamos en google `hex to text` y hacemos lo del `hash`.  

## Retos XOR, Entropia y Magic Number
XOR: Nos dan `UGFzc3dvcmQ6IHhvFzYMACEfBiAgIA==` usando una página tipo: https://conv.darkbyte.ru/ descodificamos el texto en base64. Podemos ver que el equivalente en texto es algo asi como `Password: ...`. Recortamos el inicio del texto en base64 para quedarnos solo con lo que es la contraseña como tal. En este caso queda `IHhvFzYMACEfBiAgIA==`, de esto nos quedamos con la base que queramos, binario, hexadecimal... Y nos vamos a una página como: http://xor.pw/ y desciframos el texto con la clave que nos dan `encryptXOR` (imprimid el resultado en ASCII para tener la contraseña directamente). Luego hacemos lo del `hash`.  

Entropia: No se como llegué a la solución, pero es la del `cello-2830670_1920.jpg`.  

Magic Number: Usando `xxd [archivo] | head` imprimimos el principio del archivo, con lo que se ve que es `ftypmp42` con el magic number `0000 0020 6674 7970 6d70 3432`. Hacemos `echo -n "00000020667479706D703432" | md5sum`.  

## Retos Strings, Metadatos, Metadatos2
Strings: Usamos el comando `strings archivo | grep www` y listo.  

Metadatos: Usamos `exiftool archivo` y buscamos el autor.  

Metadatos2: Usamos `exiftool archivo` y buscamos el modelo de la camara.

## Retos Variable, Variable2 y C
Variable: La variable `max` esta mal. Un string asignado a un int.  

Variable2: `echo -n "echo \"Atenea\"" | md5sum.  

C: Se compila con `gcc` y ejecutamos.

## Retos Python y Java
Python: Para resolver el reto, primero necesitaremos tener instalado el modulo de python Crypto (deberia valer con un `pip install pycrypto` o `pip install crypto` no recuerdo cual de los dos era) luego nos interesa la variable `result`. Para imprimir una variable en python usamos la función `print()` por lo tanto en este caso, añadiendo al final `print(result)` y ejecutando se nos mostrará el flag.  

Java: Nos dan un archivo .class de java, estos archivos pueden ser descompilados con herramientas online o en nuestro caso usando `jad`. Ejecutamos `jad archivo` y aparece `archivo.jad` lo abrimos, leemos el nombre de las varibales y abamos encontrando el flag.
