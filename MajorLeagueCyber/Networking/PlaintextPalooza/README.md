# Plaintext Palooza
Using unencrypted connections like HTTP put your data at risk. People can steal your information by capturing the data that you send over an unsecured network like wifi at a coffeehouse.

See if you can figure out the password that this user used when he logged into a tech support forum over HTTP.

# Solution

Paso 1: Coger `wireshark` y abrir el archivo `.pcap`.  
Paso 2: Filtrar por `http.request.protocol==POST` luego nos vamos abajo del todo, y una de las últimas sino la última de las peticiones http `POST /forums/login.php` tiene la info de usuario y contraseña.
Paso 3: El flag, es obviamente, la contraseña.
