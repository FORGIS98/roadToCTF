# Secret Document
We subpoenaed the internet traffic of a John Doe. Can you find out what he's been up to?

# Solucion
Abrinos el archivo con `wireshark` y vemos que en el trafico en `FTP` el usuario pide varias fotos y documentos. Entre otros, un documento llamado `secret document.pdf`. Cuando encontremos la primera transaccion (es la #439) lo abrimos (click derecho, follow TCP stream) y copiamos la info pero en hexadecimal (se puede cambiar abajo). Lo pegamos en un archivo, borramos todo lo que no sean los numeros en hexadecimal (osea, las direcciones de memoria y la representación ascii de la derecha) y luego ejecutamos `xxd -r -p archivo > archivo.pdf` y listo, el flag esta en el pdf.
