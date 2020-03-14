# Hurgando En El Router

Durante la investigación de un incidente de seguridad se ha obtenido el firmware de un router TP-LINK WA801ND. Para superar este reto deberás obtener la contraseña de root del dispositivo.  

# Solucion

Paso 1: Ejecutamos el comando `binwalk` para sacar todos los archivos reconocibles: `binwalk -e frw-...`. Esto sacará una carpeta (la cual no incluyo en github por ser muy grande)  
Paso 2: Dentro de la carpeta buscamos los archivos `passwd` y `shadow` los cuales estan en la carpeta `etc`. En mi caso los he copiado fuera de la carpeta para trabajar con ellos.  
Paso 3: Usaremos la herramienta `john` (john the ripper) para forzar el hash de root. Recomiendo borrar las demas lineas de ambos archivos, y quedaros solo con `root` ya que es la que nos interesa. Asi `john` tardara menos en trabajar. Ejecutamos primero `unshadow passwd.txt shadow.txt > passwords.txt` para `john` pueda leer el archivo correctamente y trabajar con el.  
Paso 4: Utilizando un diccionario como `rockyou.txt` el cual podeis buscar en google, ejecutamos `john` con el diccionario contra el archivo `passwords.txt`. En menos de un minuto, encuentra la contraseña.  
