# Juegos De Guerra
Se tienen sospechas de que en la siguiente imagen está escondida, de alguna manera, una contraseña. ¿Eres capaz de localizarla?  

# Solucion

Paso 1: Con `exiftool` analizamos los metadatos de la imagen, vemos que hay un `thumbnail` y procedemos a extraerlo con `exiftool -b -ThumbnailImage <img> <output>`.  
Paso 2: Con `file` vemos que el output es otra imagen, asi que usamos `exiftool` de nuevo, y vemos 2 cosas. La primera, tiene otro "thumbnail" la segunda, hay datos `GPS` pero solo la Latitud.  
Paso 3: Repite el paso 2 pero con la imagen que acabas de conseguir. Ejecutamos `file` y sorpresa, otra imagen. Bien, con `exiftool` vemos que no hay mas "thumbnails" pero tenemos otro dato `GPS`. En este caso, la Longitud.  
Paso 4: Vamos a `google maps`, metemos las coordenadas, ponemos el modo satelite para ver que hay en el suelo de las coordenadas. Y vemos una palabra, la cual es el flag.
