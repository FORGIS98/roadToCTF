# Micro-CMS v1

## Flag 1: XSS
En la página web se nos deja crear nuevas páginas. Al crearlas, y volver a la HOME aparecen listadas (aparecen las que hayamos creado). Lo interesante aquí es que los detalles de la nueva página se ven reflejadas en la respuesta. Por tanto hay algo que procesa la info que nosotros creamos. Por lo tanto probamos a ver si la página es vulnerable a XSS (Cross-site scripting), le metemos como nombre `hola <script>alert(1);</script>` y al volver a la HOME nos darán el primer flag.  

Hay muchos otros scripts que se pueden ejecutar, incluso uno puede aprovecharse no solo de las etiquetas de `<script>` sino también cosas como `<DIV STYLE="background-image: url(javascript:alert('XSS'))">` o `<DIV STYLE="background-image: url(javascript:alert('XSS'))">` o `<IMG SRC=X ONERROR="alert(/XSS/)">`.  

## Flag 2
