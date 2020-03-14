# DurinsGates

Informaciones fidedignas han revelado que cierto grupo de atacantes utilizan técnicas de esteganografía y cifrado junto con determinados servicios online para comunicarse entre ellos y compartir información confidencial. Recientemente se ha podido interceptar una de las imágenes empleadas para compartir este tipo de mensajes. Se sospecha que la imagen se ha enviado para remitir una clave compartida con la que es posible acceder a uno de los servicios en la nube utilizados por los atacantes.  

Tu objetivo será investigar el fichero adjunto .jpg y averiguar si está relacionado con una clave o mensaje de estas características.  

# Solucion

Paso 1: Con la herramienta `steghide` intentamos extraer la información escondida. Pero nos pide una contraseña.  
Paso 2: La foto es del señor de los anillos, por lo tanto cogemos y buscamos ese fragmento en google. Encontraremos que para abrir las puertas Gandalf usa la palabra clave `Mellon`.  
Paso 3: Vuelta a `steghide` y con la contraseña `Mellon` sacamos un archivo con una `url`.  
Paso 4: Ir a la url, copiamos el texto y lo guardamos en un archivo `base64.txt`.  
Paso 5: Con el comando `base64` desciframos el texto y lo guardamos en otro archivo `encrypted.enc`.  
Paso 6: Con el comando `file` vemos que tipo de archivo es, y vemos que es `openssl enc'd data with salted password`.  
Paso 7: Utilizamos el siguiente comando `openssl enc -aes-256-cbc -d -md MD5 -in encrypted.txt -out flag` es importante avisar que hay otro comando `openssl enc -aes-256-cbc -d -in encrypted.txt -out flag` pero no va, https://stackoverflow.com/questions/39637388/encryption-decryption-doesnt-work-well-between-two-different-openssl-versions. El caso, nos pide una contraseña, cual?  
Paso 8: Con el comando `exiftool` analizamos los metadatos de la imagen original, y vemos que el artista es: 68913499125FAA, sospechoso no? Probamos el comando del paso 8 y ponemos esa contraseña.  
Paso 9: Conseguimos un archivo `flag`, aun no sabemos que es el flag, de hecho, que es? Pues con el comando `file flag` vemos que se trata de un archivo `MP4`, procedemos a reproducirlo y bingo, tenemos el flag.  
