Algoritmo sin_titulo
	//get data 
	//identify finally process
	//1st level(grade 1): 30%
	//2nd level (grade 2) : 30%
	//3rd level (grade 3) : 40%
	
	//step one : definiri variable // y // step two blaquear variables , que es bblaquear las variables  grades=0 caracter =""//
	Definir  name como caracter
	definir grade1, grade2, grade3,notafin Como Real
	//step3: read name and grades
	escribir "enter student name"
	leer name 
	escribir "enter grades"
	leer grade1, grade2, grade3
	//step 3 process calculate//
	
	notafin= 0.3*grade1 + 0.3*grade2 + 0.4*grade3
	//output result
	escribir "compañero UNICESMAG: "  + nombre , "your final note is: "  notafin 
	escribir "grades averages is : " (grade1+grade2+grade3)/3
FinAlgoritmo
