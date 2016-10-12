import random
import time

class Player:
    def __init__(self,health,strength):
        self.health = int(health)
        self.strength = int(strength)
    def hit(self,damage):
        self.health -= damage

def status():
    return 'You: ' + str(hero.health) + '\tEnemy: ' + str(enemy.health) + '\n'

print ''
hero = Player(raw_input('Your health: '), raw_input('Your strength: '))
print ''
enemy = Player(raw_input('Enemy health: '), raw_input('Enemy strength: '))

print '\n'

while hero.health > 0 and enemy.health > 0 :

    enemy_attack = random.randint(0, enemy.strength)
    print 'You were hit for ' + str(enemy_attack) + ' hitpoints!'
    hero.hit(enemy_attack)
    print status()
    time.sleep(2)

    if hero.health < 0 :
        break

    hero_attack = random.randint(0, hero.strength)
    print 'You hit enemy for ' + str(hero_attack) + ' hitpoints!'
    enemy.hit(hero_attack)
    print status()
    time.sleep(2)

if hero.health < 0 :
    print 'GAME OVER!'
else:
    print 'You win! :D'
