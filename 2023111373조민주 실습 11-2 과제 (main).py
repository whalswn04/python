from character import Hero, Monster
from battle import Battle

def main():
    print("게임 시작")
    name = input("이름 입력:")
    role = input("직업 입력(전사/마법사/궁수)")
    hero = Hero(name,100,20,5,speed=12,role=role)
    print(hero)
    monster = Monster("고블린",30,10,2,speed=10, level=1)
    print(monster)
    battle = Battle()
    for i in range(5):
        battle.fight(hero,monster)
        monster.level_up()

    print(hero)

if __name__ == '__main__':
    main()