# Primer versión de Calculadora
## Procedimiento:
![imag](https://user-images.githubusercontent.com/28718644/49244619-fbf98580-f3ee-11e8-9657-9a8d7c1c0225.jpg)

![imag2](https://user-images.githubusercontent.com/28718644/49250407-80530500-f3fd-11e8-8bcd-84686aee7b7e.png)


## Explicación:
Este primer proyecto fue realizado con conocimientos básicos de programación.<br />
Consta de 3 archivos:<br />
                      1. **Calculadora.py** : Main del programa. Se encanga de tomar datos del usuario e imprimir el resultado.<br />
                      2. **Encontrar_Parentesis**: Encuentra las posiciones dentro del string de todos los paréntesis. Resuelta la expresión 
                                          dentro de ellos, rearma el string para ser evaluado nuevamente.<br />
                      3. **Resolver_Cuenta**: Esta función recibe un string ***sin paréntesis*** y se encarga de resolver la operación que 
                                              representa, utilizando la lógica de prioridades matemáticas. Devuelve un float con el resultado<br />

## Errores tenidos en cuenta y por lo tanto salvados:

- En **Calculadora.py**: input() -> Solo operadores y números válidos.
- En **Encontrar_Parentesis**: Cantidad dispar de paréntesis.
- En **Resolver_Cuenta**: División por cero.

## Recursividad:

En **Encontrar_Parentesis** se utilizó el concepto de recursividad, es decir, llamar a la función dentro de la misma función. 

¿Por qué se hizo esto? Como mencioné anteriormente, esta función encuentra los paréntesis, manda a resolver la expresión dentro de ellos
y rearma el string con el resultado. Como dentro de este string aún pueden haber más pares de paréntesis, se debe volver a buscar
las posiciones de estos dentro del ***nuevo string*** (O sea, que las posiciones anteriores ya no sirven).

El proceso sigue hasta que ya no queden expresiones por resolver. Para que no se entre en un loop infinito se utilizaron flags. 
`fin_calculo = True`.


### Autor: Brian Reinke.  Versión: 1.0.0
