
oponent_choosen_pokemon = input("¿Contra que pokemon quieres luchar? (Squirtle/Charmander/Bulbasaur :")
pikachu_life = 100
if oponent_choosen_pokemon == "Squirtle":
    enemy_pokemon_life = 90
if oponent_choosen_pokemon == "Charmander":
    enemy_pokemon_life = 80
if oponent_choosen_pokemon == "Bulbasaur":
    enemy_pokemon_life = 100
else:
    enemy_pokemon_life = 0

while pikachu_life > 0 and enemy_pokemon_life > 0:
    choosen_movement = input("¿Qué ataque vamos a usar? Chispazo/Bola Voltio:")
    if choosen_movement == "Chispazo":
        enemy_pokemon_life -= 10
    if choosen_movement == "Bola Voltio":
        enemy_pokemon_life -= 12
    print("La vida del enemigo ahora es de {}".format(enemy_pokemon_life))
    if oponent_choosen_pokemon == "Squirtle":
        print("Squirtle te hace un ataque de 8 de daño")
        pikachu_life -= 8
    if oponent_choosen_pokemon == "Charmander":
        print("Charmander te hace un ataque de 7 de daño")
        pikachu_life -= 7
    if oponent_choosen_pokemon == "Bulbasaur":
        print("Bulbasaur te hace un ataque de 10 de daño")
        pikachu_life -= 10
    print("La vida de tu pokemon ahora es de {}".format(pikachu_life))
if enemy_pokemon_life <= 0:
    print("¡Has ganado!")
if pikachu_life <= 0:
    print("¡Has perdido!")


print("El combate se ha terminado")
