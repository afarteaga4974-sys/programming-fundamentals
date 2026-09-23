Algoritmo SalarioSemanal
	
	// Definir variables
	Definir nombre Como Cadena
	Definir horasTrabajadas, valorHora, salarioTotal Como Real
	
	// Inicializar variables
	nombre <- ""
	horasTrabajadas <- 0
	valorHora <- 0
	salarioTotal <- 0
	
	// Solicitar datos
	Escribir "Ingrese el nombre del trabajador:"
	Leer nombre
	
	Escribir "Ingrese el numero de horas trabajadas:"
	Leer horasTrabajadas
	
	Escribir "Ingrese el valor pagado por cada hora:"
	Leer valorHora
	
	// Procesar calculo
	salarioTotal <- horasTrabajadas * valorHora
	
	// Mostrar resultado
	Escribir "Trabajador: ", nombre
	Escribir "El salario total semanal es: $", salarioTotal
	
FinAlgoritmo
