## Uso

1. Clona este repositorio o descarga el archivo `fuerza_bruta.py`.
2. Ejecuta el programa con Python:

   ```sh
   python fuerza_bruta.py

3. Ingresa la contraseña que deseas adivinar cuando se te solicite. Nota: La contraseña puede consistir en letras mayúsculas o minúsculas, ya que el programa las considera equivalentes.

4. El programa mostrará cuántos intentos fueron necesarios para adivinar la contraseña.

- Ejemplo

Si ingresas la contraseña abc, el programa realizará las siguientes comparaciones:
a es igual a a => Sí (1 intento), continúa con la siguiente letra.
b es igual a a => No (2 intentos), prueba otra comparación.
b es igual a b => Sí (3 intentos), continúa con la siguiente letra.
c es igual a a => No (4 intentos), prueba con otra comparación.
c es igual a b => No (5 intentos), prueba con otra comparación.
c es igual a c => Sí (6 intentos), continúa con la siguiente letra.

El resultado será:
La contraseña se adivinó en 6 intentos.

6. Código

Aquí está el código del programa:


7. Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia, por favor abre un issue o envía un pull request.