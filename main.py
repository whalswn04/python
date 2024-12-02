from character import Hero, Monster
from battle import Battle

def main():
    print("게임 시작")
    name = input("이름 입력:")
    role = input("직업 입력(전사/마법사/궁수)")
    hero = Hero(name,100,20,5,speed=12,role=role)
    print(hero)

    monster_pool=[
        goblin(name:"고블린",hp:50,attack:10,defence:5),
        orc(name:"오크",hp:80,attack:15,defence:7),
        dragon(name:"드래곤",hp:150,attack:50,defence:30),
    ]
    battle = Battle()
    while hero.is_alive():
        monster = random.choice(monster_pool)
        print(f"/n 몬스터{monster.name} 등장!")
        print(monster.description())

if __name__ == '__main__':
    main()