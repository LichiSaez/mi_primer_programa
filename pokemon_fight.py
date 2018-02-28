
oponent_choosen_pokemon = input("¿Contra que pokemon quieres luchar? (Squirtle/Charmander/Bulbasaur :")
pikachu_life = 100
if oponent_choosen_pokemon == "Squirtle":
    enemy_pokemon_life = 90
    opponent_pokemon = "Squirtle"
    enemy_pokemon_damage = 8
elif oponent_choosen_pokemon == "Charmander":
    enemy_pokemon_life = 80
    opponent_pokemon = "Charmander"
    enemy_pokemon_damage = 7
elif oponent_choosen_pokemon == "Bulbasaur":
    enemy_pokemon_life = 100
    opponent_pokemon = "Bulbasaur"
    enemy_pokemon_damage = 10
else:
    enemy_pokemon_life = 0
    enemy_pokemon_damage = 0
while pikachu_life > 0 and enemy_pokemon_life > 0:
    choosen_movement = input("¿Qué ataque vamos a usar? Chispazo/Bola Voltio:")
    if choosen_movement == "Chispazo":
        enemy_pokemon_life -= 10
    elif choosen_movement == "Bola Voltio":
        enemy_pokemon_life -= 12
    print("La vida del {} ahora es de {}".format(opponent_pokemon, enemy_pokemon_life))
    print("{} te hace un ataque de {} de daño".format(opponent_pokemon,enemy_pokemon_damage))
    pikachu_life -= enemy_pokemon_damage
    print("La vida de tu pokemon ahora es de {}".format(pikachu_life))
if enemy_pokemon_life <= 0:
    print("¡Has ganado!")
if pikachu_life <= 0:
    print("¡Has perdido!")


print("El combate se ha terminado")
