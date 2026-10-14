#juego de dados
import random

# Pedir el nombre del jugador
nombre = input("Ingresa tu nombre: ")

# Inicializar variables
vidas = 5
total_tiradas = 0
sumas_pares = 0
sumas_impares = 0
dados_iguales = 0
suma_total = 0

print("\n¡Bienvenido al juego de dados,", nombre, "!")
print("Comienzas con", vidas, "vidas.")

# Iniciar el juego
while vidas > 0:

    input("\nPresiona ENTER para lanzar los dados...")

    # Lanzar los dos dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    # Calcular la suma
    suma = dado1 + dado2

    # Actualizar contadores
    total_tiradas += 1
    suma_total += suma

    print("\nDado 1:", dado1)
    print("Dado 2:", dado2)
    print("Suma:", suma)

    # Contar dados iguales
    if dado1 == dado2:
        dados_iguales += 1
        print("¡Los dados son iguales!")

    # Verificar si salen dos unos
    if dado1 == 1 and dado2 == 1:
        if vidas >= 1:
            print("\n¡FELICIDADES! ¡HAS GANADO!")
            break

    # Aplicar las reglas de las sumas
    if suma % 2 == 0:
        sumas_pares += 1

        if vidas < 5:
            vidas += 1

        print("La suma es par. Ganas una vida si tienes menos de 5.")

    else:
        sumas_impares += 1
        vidas -= 1
        print("La suma es impar. Pierdes una vida.")

    print("Vidas actuales:", vidas)

    # Comprobar si el jugador pierde
    if vidas == 0:
        print("\nGAME OVER: ¡HAS PERDIDO!")
        break

# Mostrar el informe final
print("\n========== INFORME FINAL ==========")
print("Jugador:", nombre)
print("Total de tiradas:", total_tiradas)
print("Tiradas con sumas pares:", sumas_pares)
print("Tiradas con sumas impares:", sumas_impares)
print("Tiradas con dados iguales:", dados_iguales)
print("Suma total de los dados:", suma_total)
print("Vidas restantes:", vidas)
print("===================================")

