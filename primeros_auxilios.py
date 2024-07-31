#- Primeros auxilios
#En cualquier momento puede haber una emergencia y hay que estar preparados ¿sabrías
#cómo reaccionar en caso de que alguien necesite de primeros auxilios?
#Es muy probable que mucha gente no conozca cuáles son los pasos a seguir en caso de emergencia. Es por eso que se le solicita construir una aplicación que permita indicar los
#pasos a seguir ante una emergencia. Debido a que no se espera que usted sea un experto en el tema se le provee de un diagrama que explica las distintas instancias a la que se está
#sometido durante una emergencia.

#Primero defino la varibale de la pregunta si responde a estímulos o no
responde_a_estimulos = input("¿El paciente responde a estímulos? Responda si o no: ")
if responde_a_estimulos == "si":
    print("Valorar la necesidad de llevarloal hospital más cercano")
elif responde_a_estimulos == "no":
    print("Abrir la vía aérea")

#Variable para saber que hacer si el paciente respira o no
respira = input("¿El paciente respira? Responda si o no: ")
