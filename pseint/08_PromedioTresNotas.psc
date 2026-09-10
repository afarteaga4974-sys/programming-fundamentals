Algoritmo PromedioTresNotas
	
	// Definir variables
	Definir nombre Como Cadena
	Definir nota1, nota2, nota3, promedio Como Real
	
	// Inicializar variables
	nombre <- ""
	nota1 <- 0
	nota2 <- 0
	nota3 <- 0
	promedio <- 0
	
	// Solicitar datos
	Escribir "Ingrese el nombre del estudiante:"
	Leer nombre
	
	Escribir "Ingrese la primera calificacion:"
	Leer nota1
	
	Escribir "Ingrese la segunda calificacion:"
	Leer nota2
	
	Escribir "Ingrese la tercera calificacion:"
	Leer nota3
	
	// Procesar calculo
	promedio <- (nota1 + nota2 + nota3) / 3
	
	// Mostrar resultado
	Escribir nombre, ", el promedio de sus calificaciones es: ", promedio
	
FinAlgoritmo
