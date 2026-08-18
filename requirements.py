#Con eso, el flujo completo queda bien definido:

#Usuario indica carpeta, prefijo y/o sufijo
#Programa calcula los nuevos nombres → guarda la lista de pares {'old_name', 'new_name'} en una variable
#Programa muestra el dry run (cómo quedarían los nombres) — todavía no toca ningún archivo
#Usuario confirma
#Programa ejecuta el renombrado real usando la lista ya calculada
#Si el usuario se arrepiente después de ejecutar, puede usar la misma lista en memoria para hacer undo (renombrar de vuelta al nombre viejo)

START_NUMBER = 1
NUMBER_DIGITS = 3
FORBIDDEN_CHARACTERS = '@\/<>*?:"'



