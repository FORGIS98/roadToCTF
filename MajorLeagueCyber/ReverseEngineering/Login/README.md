# Login
You've been tasked by law enforcement to break into the secret safe of Nefarious Incorporated.

You've found the door to the safe room. But it's protected by a computerized login system...

root@13ea019f8a92:~# ./login
Error: ./login <password>

To get in you'll need the password...

But it looks like you can run commands on the login system. Maybe you can extract the password from the program?

# Solution

Lo lógico es usar una herramienta tipo `radare2` o `cutter` que viene a ser una interfaz gráfica de radare2. Pero al estar el password a palo seco pues con el comando `strings` podemos imprimir todo lo que es legible del ejecutable. Y con `strings -n 7 archivo` para solo mostrar cosas que tengan mas de 7 caracteres (o 7) pues tenemos el flag. Pongo 7 pero podeis poner 10 o podeis hacer `strings archivo | grep flag` y listo. Solo que no siempre viene laplabra flag.
