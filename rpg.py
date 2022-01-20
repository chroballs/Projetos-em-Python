import random

#Herois

class Kim(object):
    name = "Kim"
    hp = 150
    mp = 200
    defesa = 20
    fisico = 5
    magic = 15
    power = 50

class Striker(object):
    name = "Striker"
    hp = 200
    mp = 90
    defesa = 20
    fisico = 10
    magic = 15
    power = 50
    
class Jason(object):
    name = "Jason"
    hp = 173
    mp = 150
    defesa = 20
    fisico = 10
    magic = 15
    power = 75
    
#Inimigo

class Puppet(object):
    name = "Puppet"
    hp = 200
    mp = 100
    fisico = 10
    ataque1 = 30
    ataque2 = 30
    loot = random.randint(0,2)

class Viper(object):
    name = "Viper"
    hp = 200
    mp = 100
    fisico = 30
    ataque1 = 30
    ataque2 = 30
    loot = random.randint(0,2)

class Tornado(object):
    name = "Tornado"
    hp = 200
    mp = 100
    fisico = 30
    ataque1 = 15
    ataque2 = 30
    loot = random.randint(0,2)

def gameOver(character):
    if character.hp < 1:
        print("Que mico...")
        print("Mas não desista, tente denovo!")
        print("")
        exit()
    

def heroselect():
    print("Escolha seu heroi!")
    selection = input("1. Kim \n2. Striker \n3. Jason \n")
    if selection == "1":
        character = Kim
        print("Ah, que maravilha... Tava mesmo com vontade de chutar bundas depois da escola")
        print("HP - ", character.hp)
        print("MP - ", character.mp)
        print("Defesa - ", character.defesa)
        print("Ataque Fisíco - ", character.fisico)
        print("Ataque 1: Bolhas Volateis - ", character.magic)
        print("Ataque 2: T-REX - ", character.power)
        return character

    elif selection == "2":
        character = Striker
        print("Hora da festa de boas-vindas!")
        print("HP - ", character.hp)
        print("MP - ", character.mp)
        print("Defesa - ", character.defesa)
        print("Ataque Fisíco - ", character.fisico)
        print("Ataque 1: Deadly Skyte - ", character.magic)
        print("Ataque 2: Peledaki - ", character.power)
        return character

    elif selection == "3":
        character = Jason
        print("*Sons de baforo* Vamo lá.")
        print("HP - ", character.hp)
        print("MP - ", character.mp)
        print("Defesa - ", character.defesa)
        print("Ataque Fisíco - ", character.fisico)
        print("Ataque 1: Flame Flare - ", character.magic)
        print("Ataque 2: Monferno - ", character.power)
        return character

    else:
        print("Pressione 1, 2 ou 3 para continuar")
        heroselect()


def enemyselect(Puppet,Viper,Tornado):
    enemyList = [Puppet,Viper,Tornado]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["poção", "encantamento de cura", "cachaça curandeira"]
    lootDrop = loot[lootChance]
    return lootDrop

def battlestate():
    enemy = enemyselect(Puppet,Viper,Tornado)
    print("Misericordia...",enemy.name, "do Esquadrão Escarlate!")
    print("Você tem três formas de superar este combate:")
    while enemy.hp > 0:
        choice = input("1.Ataque Fisíco\n2. Ataque 1\n3. Ataque 2\n4. Corra!")

        if choice == "1":
            mp = 15
            print("Pegue seus dedinhos e desfira um tapa contra", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 10:
                enemy.hp = enemy.hp - character.fisico
                print("Caraca! Seu golpe no inimigo foi tão bom que o deixou com...", enemy.hp)

                if enemy.hp > 0:
                    character.hp = character.hp - (enemy.fisico / character.defesa)
                    print("A", enemy.name,"deu a volta por cima e te deixou no chinelo, deixando você com", character.health)
                    gameOver(character)

                else:
                    if enemy.name == "Puppet":
                        enemy.hp = 200

                    elif enemy.name == "Viper":
                        enemy.hp = 200

                    elif enemy.name == "Tornado":
                        enemy.hp = 200

                    print("Você derrotou", enemy.name)
                    break


            else:
                print("Você tá muito cagado para isso, quem sabe mais tarde")
                print("A", enemy.name, "te deu um golpe com o mais puro odio")
                character.hp = character.hp - enemy.fisico
                print("Agora você está com",character.hp,"restante")
                gameOver(character)

        if choice == "2":
            mp = 15
            print("Tava doidinho(a) pra usar né? Lá vai seu ataque poderoso", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 20:
                enemy.hp = enemy.hp - character.magic
                print("Caraca! Seu golpe no inimigo foi tão bom que o deixou com...", enemy.hp)

                if enemy.hp > 0:
                    character.hp = character.hp - (enemy.fisico / character.defesa)
                    print("A", enemy.name,"deu a volta por cima e te deixou no chinelo, deixando você com", character.health)
                    gameOver(character)

                else:
                    if enemy.name == "Puppet":
                        enemy.hp = 200

                    elif enemy.name == "Viper":
                        enemy.hp = 200

                    elif enemy.name == "Tornado":
                        enemy.hp = 200

                    print("Você derrotou", enemy.name)
                    break


            else:
                print("Você tá muito cagado para isso, quem sabe mais tarde")
                print("A", enemy.name, "te deu um golpe com o mais puro odio")
                character.hp = character.hp - enemy.fisico
                print("Agora você está com",character.hp,"restante")
                gameOver(character)

        if choice == "3":
            mp = 15
            print("Tava doidinho(a) pra usar né? Lá vai seu ataque poderoso", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 15:
                enemy.hp = enemy.hp - character.power
                print("Caraca! Seu golpe no inimigo foi tão bom que o deixou com...", enemy.hp)

                if enemy.hp > 0:
                    character.hp = character.hp - (enemy.fisico / character.defesa)
                    print("A", enemy.name,"deu a volta por cima e te deixou no chinelo, deixando você com", character.health)
                    gameOver(character)

                else:
                    if enemy.name == "Puppet":
                        enemy.hp = 200

                    elif enemy.name == "Viper":
                        enemy.hp = 200

                    elif enemy.name == "Tornado":
                        enemy.hp = 200

                    print("Você derrotou", enemy.name)
                    break


            else:
                print("Você tá muito cagado para isso, quem sabe mais tarde")
                print("A", enemy.name, "te deu um golpe com o mais puro odio")
                character.hp = character.hp - enemy.fisico
                print("Agora você está com",character.hp,"restante")
                gameOver(character)

        if choice == "4":
            print("Vai 'pa' onde, flor?")

    
character = heroselect()
battlestate()
battlestate()
battlestate()

