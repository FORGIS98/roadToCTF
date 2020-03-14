# Passcode
Ok you're in the secret safe room. The safe itself looks physically intimidating but it has a small key pad.  

On the safe it looks like they switched the password for a passcode....  

root@13ea019f8a92:~# ./passcode  
Please enter your passcode: 12345678  
[ACCESS DENIED]  

To break into the safe you'll need to figure out the passcode. Maybe this program is like the door and saves the keycode inside of itself somehow.  

The passcode is the flag.  

# Solution

Esta vez si que vamos a usar radare2. Vamos poco a poco.  
Paso 1: Primero tengamos algo de info básica sobre el ejecutable con `rabin2 -I passcode` y `rabin2 -z passcode`.  
Paso 2: Abrimos `radare2 archivo` y ejecutamos un analisis general `aaa` y le dais al enter. Luego con el comando `s main` os movereis al main (se puede ver que la direccion de memoria ha cambiado).  
Paso 3: Con `VV` vemos el flujo de la función main. Si lo seguimos, vemos que llega un punto en el que se compara `cmp eax, 0x...` donde `eax` es lo que hemos metido por pantalla. Luego vemos que tras la comparación se va a verdadero o cierto, un poco como un `if`. Por tanto ese ha de ser el flag, eso si, pasadlo a decimal.  

PD: Para salir de radare dadle a la `q` hasta que salgais del modo "grafico" o "visual" y luego le dais a la `q` otra vez y al enter.

