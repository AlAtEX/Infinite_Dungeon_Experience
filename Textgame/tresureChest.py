import itemGen, time
def get(Weapon,Armor,hp,mhp,xp,level,mi,ma):
    print('You found a tresure chest!')
    items = itemGen.tresureGen(level,mi,ma,mhp)
    for item in items:
        print(item['desc'])
        time.sleep(1)
        if item['type'] == 'st':
            if Weapon < item['mod']:
                Weapon = item['mod']
                print('Your damage is now {a}!'.format(a = Weapon))
        if item['type'] == 'ar':
            if Armor < item['mod']:
                Armor = item['mod']
                print('Your defence is now {a}!'.format(a = Armor))
        if item['type'] == 'hp':
            hp += item['mod']
            if hp > mhp:
                hp = mhp
                print('You were healed {a}HP!'.format(a = item['mod']))
        if item['type'] == 'mhp':
            mhp += item['mod']
            print('Your max HP is now {a}!'.format(a = mhp))
        if item['type'] == 'xp':
            xp += item['mod']
            print('Your xp is now {a}!'.format(a = xp))
        time.sleep(1)
    time.sleep(0.5)
    print('You close the chest.')
    return Weapon,Armor,hp,mhp,xp,level
