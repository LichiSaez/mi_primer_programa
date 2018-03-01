my_list = []
user_input = input("¿Que necesitas comprar? Escribe Fin para terminar")

while user_input != "Fin":
    my_list.append(user_input)
    user_input = input("¿Que necesitas comprar? Escribe Fin para terminar")

length_list = len(my_list)
current_index = 0

while current_index < length_list:
    print("Tengo que comprar {}".format(my_list[current_index]))
    current_index += 1

print("Esta es la lista del super")
