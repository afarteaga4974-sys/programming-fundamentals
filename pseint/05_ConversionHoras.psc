Algoritmo ConversionHoras
	
	// Definir variables
	Definir horas, minutos, segundos Como Real
	
	// Inicializar variables
	horas <- 0
	minutos <- 0
	segundos <- 0
	
	// Solicitar datos
	Escribir "Ingrese la cantidad de horas:"
	Leer horas
	
	// Procesar calculos
	minutos <- horas * 60
	segundos <- horas * 3600
	
	// Mostrar resultados
	Escribir "Cantidad de minutos: ", minutos
	Escribir "Cantidad de segundos: ", segundos
	
FinAlgoritmo
