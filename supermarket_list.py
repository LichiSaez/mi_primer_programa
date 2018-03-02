my_list = []
user_input = input("¿Que necesitas comprar? Escribe Fin para terminar")

while user_input != "Fin":
    my_list.append(user_input)
    user_input = input("¿Que necesitas comprar? Escribe Fin para terminar")

length_list = len(my_list)
current_index = 0

for item in my_list:
    print("Tengo que comprar {}".format(item))
print("Esta es la lista del super")
