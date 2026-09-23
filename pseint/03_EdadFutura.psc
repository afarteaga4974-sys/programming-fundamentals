Algoritmo EdadFutura
	
	// Definir variables
	Definir nombre Como Cadena
	Definir edadActual, cantidadAños, edadFuturo Como Entero
	
	// Inicializar variables
	nombre <- ""
	edadActual <- 0
	cantidadAnios <- 0
	edadFuturo <- 0
	
	// Solicitar datos
	Escribir "Ingrese el nombre de la persona:"
	Leer nombre
	
	Escribir "Ingrese la edad actual:"
	Leer edadActual
	
	Escribir "Ingrese la cantidad de años:"
	Leer cantidadAnios
	
	// Procesar calculo
	edadFuturo <- edadActual + cantidadAños
	
	// Mostrar resultado
	Escribir nombre, " tendra ", edadFuturo, " años."
	
FinAlgoritmo