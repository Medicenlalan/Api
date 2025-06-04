# Api
Devuelve un mensaje simple.  
Esta API es como una pequeña aplicación que guarda y muestra una lista de personas (usuarios). Puedes imaginarla como una libreta de contactos digital, pero muy básica.

Tiene cuatro funciones principales:

Mostrar un mensaje de bienvenida
Cuando visitas la dirección principal (por ejemplo, http://localhost:5000/), te muestra un mensaje que dice:
"¡Bienvenido a mi API!"

Mostrar la lista de usuarios
Si vas a la dirección http://localhost:5000/usuarios, te muestra todos los usuarios guardados.
Por ejemplo: Ana y Luis.

Ver un usuario por su número (ID)
Si vas a algo como http://localhost:5000/usuarios/1, te muestra solo al usuario con ID 1.

Agregar un nuevo usuario
Puedes enviarle un nombre (por ejemplo, "Carlos") y la API lo guarda en la lista.


Paso 1: Crear el archivo
Primero, copias el código de la API y lo pegas en un archivo de texto con nombre api.py.

Paso 2: Instalar Flask
Abres la terminal (o símbolo del sistema en Windows) y escribes:

pip install flask
Esto instala la herramienta que necesitas para que la API funcione.

Paso 3: Ejecutar el archivo
Después, desde la terminal, vas a la carpeta donde guardaste el archivo y escribes:

