Algoritmo EdadActual
	
	// Definir variables
	Definir nombre Como Cadena
	Definir añoNacimiento, añoActual, edad Como Entero
	
	// Inicializar variables
	nombre <- ""
	añoNacimiento <- 0
	añoActual <- 2026
	edad <- 0
	
	// Solicitar datos
	Escribir "Ingrese el nombre de la persona:"
	Leer nombre
	
	Escribir "Ingrese el año de nacimiento:"
	Leer añoNacimiento
	
	// Procesar calculo
	edad <- añoActual - añoNacimiento
	
	// Mostrar resultado
	Escribir nombre, ", actualmente tienes ", edad, " años."
	
FinAlgoritmo
