
apetece_helado_input = input("¿Te apetece un helado? (Si/No):")
tienes_dinero_input = input("¿Tienes dinero para un helado? (Si/No):")
esta_el_senor_de_los_helado_input= input("¿Esta el señor de los helados? (Si/No)")
esta_tu_tia_input = input ("¿Estas con tu tía?")

apetece_helado = apetece_helado_input == "Si"
puede_permitirselo = tienes_dinero_input == "Si" or esta_tu_tia_input == "Si"
esta_el_señor_de_los_helados = esta_el_senor_de_los_helado_input == "Si"


if apetece_helado and puede_permitirselo and esta_el_señor_de_los_helados:
        print("Pues comete un helado")
else:
        print("Pues nada")
