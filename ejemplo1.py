"""
Calcular la nota de un estudiante, que 
tiene 2 sistematicos de 30
y uno de 40
"""
sistematico1 = int(input("Ingrese primer sistematico (max: 30): "))
sistematico2 = int(input("Ingrese segundo sistematico (max: 30): "))
sistematico3 = int(input("Ingrese tercer sistematico (max: 40): "))
nota = (sistematico1 + sistematico2 + sistematico3) 
print("La nota del estudiante es: ", nota)