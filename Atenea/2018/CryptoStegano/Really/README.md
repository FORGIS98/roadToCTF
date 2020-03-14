# Really

Durante el estudio del disco duro del ordenador de un sospechoso se ha encontrado un fichero cifrado mediante PGP. Al no encontrarse ninguna clave privada dentro del equipo se sospecha que dicho fichero esté cifrado mediante cifrado simétrico.  

Por otro lado, todas las contraseñas obtenidas de varias cuentas del sospechoso (a partir de la investigación de su equipo) tienen las siguientes características:  

- Son de longitud 6 o 7  
- Sólo contienen letras minúsculas  
- Sólo se utilizan estas letras: qwertyiopnmjk  
- No se repite ninguna de las letras de la contraseña  
- Algunas de ellas contiene únicamente un número entre estos: 013  

Ninguna de esas contraseñas ha servido para descifrar el fichero, pero quizás haya sido cifrado con una contraseña con estas mismas características.  

No sabemos si el contenido del fichero es relevante para la investigación, pero sólo hay una forma de averiguarlo...  

Pista: La lengua materna del dueño del equipo es el inglés.  

# Solucion

Paso 1: Generar un diccionario para atacar al archivo. Al ser clave simetrica y teniendo tantos datos sobre la contraseña podemos hacerlo por fuerza bruta. Para generar contraseñas se pueden usar programas, o coger el archivo `rockyou.txt` (buscad en google) y con `grep` coger solo las palabras que cumplan la descripcion: `grep -x '[qwertyiopnmjk013]\{6,7\}' ../../../../tools/rockyou.txt > wordlist.txt`  
Paso 2: Con `gpg2john message-2def3de75a007fa096097626a097930b.asc > john.asc` convertimos el archivo en un archivo de hash.  
Paso 3: Con la herramienta `john` o `john the ripper` ejecutamos `john john.asc --wordlist=wordlist.txt` y la herramienta probara cada contraseña de la wordlist. Tras unos segundos, tenemos el password. En ocasiones no aparece por pantalla, para eso usa `john --show`.  
Paso 4: Utilizar ese password para descifrar el msg con el comando `gpg -d message-2def3de75a007fa096097626a097930b.asc > messageAfterPassword.txt`.  
Paso 5: Nos encontramos ante un texto, el cual no nos aporta gran cosa a primera vista. Pero, tiene unos sospechosos espacios al final de cada linea, cada espacio de un tamaño diferente. Con un poco de busqueda en google, encontramos que esa información escondida puede ser descifrada con un programa llamado `snow`. Por tanto, usamos `snow` y el archivo de salida que nos da es una receta.  
Paso 6: Copiamos la receta, la pegamos en google y el flag es el nombre de la receta, 2 veces y en minusculas.  
