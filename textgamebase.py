import Inputs, time, sys, random
def story(text, inptext, mi, ma):
    print(text)
    inum = 1
    for ch in inptext:
        print(str(inum) + ": " + ch)
        inum += 1
    choice = Inputs.num(mi, ma)
    return choice
#fchoice = story("You wake up in a cave.", ["Run","Hide"],1,2)
def sdie(dtype):
    if dtype == 'Fight':
        print("Maybe you should've aimed for the groin?")
    if dtype == 'Trap':
        print("Watch out for the-Oh, nevermind.")
    time.sleep(1)
    sys.exit()
def fight(hp, mhp, st, ar, ehp, emhp, est, ear, ename, encounter, deathtext, edeathtext, loot): #hp = health, mhp = maximum health, st = Damage, ar = Damage reduction
    Gold = 0
    Armor = 0
    Weapon = 0
    print(encounter)
    alive = True
    time.sleep(2)
    infight = True
    while infight:
        dod = False
        print('You have {a}/{b} HP, do {c} Damage and have an armor rating of {d}'.format(a = hp, b = mhp, c = st, d = ar))
        time.sleep(2)
        print('The {e} has {a}/{b} HP, does {c} Damage and has an armor rating of {d}'.format(a = ehp, b = emhp, c = est, d = ear, e = ename))
        time.sleep(2)
        fof = story('What do you do? Do you:', ["Attack","Run"],1,2)
        if fof == 1:
            dod = True
        if fof == 2:
            prob = random.randint(1,3) 
            if prob == 1 or prob == 2:
                print('You got away!')
                infight == False
                break
            else:
                dod = True
                print('You could not run.')
        if dod:
            if (st - ear) > 0:
                ehp -= (st - ear)
            elif (st - ear) <= 0:
                print("Your attack of {a} did nothing to the {c}'s armor of {b}.".format(a = st, b = ear, c = ename))
                time.sleep(1)
                
            if (est - ar) > 0:
                hp -= (est - ar)
            elif (est - ar) <= 0:
                print("The {a}'s attack of {b} did nothing to your armor of {c}.".format(a = ename,  b = est, c = ar))
                time.sleep(1)
        if hp <= 0:
            print(deathtext)
            infight = False
            alive = False
        elif ehp <= 0:
            print(edeathtext)
            if loot['Gold'] != False:
                Gold += loot['Gold']
                print('You got {a} Gold!'.format(a = Gold))
                time.sleep(1)
            if loot['Weapon'] != False:
                if loot['Weapon'] > st:
                    Weapon = loot['Weapon']
                    print('Your attack is now {a}, by getting a new weapon!'.format(a = Weapon))
                    time.sleep(1)
                else:
                    Weapon = st
            else:
                Weapon = st
            if loot['Armor'] != False:
                if loot['Armor'] > ar:
                    Armor = loot['Armor']
                    print('Your Armor is now {a}, by getting new Armor!'.format(a = Armor))
                    time.sleep(1)
                else:
                    Armor = ar
            else:
                Armor = ar
            infight = False
    return alive, Gold, Armor, Weapon, hp
#fight(100,100,5,1,10,10,5,0,"dog","WOOF","AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH","Stupid Mutt.",{'Gold':10,'Weapon':10,'Armor':2})
#alive, gp, Armor, Weapon, hp = fight(currentHP,maximunHP,damage,armor,currentEnemyHP,maximumEnemyHP,EnemyAttack,EnemyArmor,EnemyName,EncounterText,DeathText,EnemyDeathText,Drops)
#Gold += gp
def trap(name,text,survivetext,damage,hp, mhp):
    print(text)
    time.sleep(1)
    alive = True
    hp -= damage
    print("The {a} did {b} damage, you now have {c}/{d} HP.".format(a = name, b = damage, c = hp,d = mhp))
    time.sleep(1)
    if hp <= 0:
        alive = False
    else:
        print(survivetext)
    time.sleep(1)
    return hp, alive
#hp, alive = trap("Pit","You fall into a pit, walking carelessly.","You learn to NOT fall into pits.",10,hp,mhp)
def store(entertext,items, gold, armor, weapon, hp, mhp, exittext, xp, level):
    print(entertext)
    time.sleep(1)
    while True:
        print('You have {a} Gold, {b} Armor rating, {c} Damage and {d}/{e} HP. You are level {f} and have {g}/{h} xp'.format(a = gold, b = armor, c = weapon, d = hp, e = mhp, f = level, g = xp, h = (level * 25)))
        for itemindex in range(0, len(items)):
            print('{c}: {a} | price: {b}'.format(a = items[itemindex]['desc'], b = items[itemindex]['price'],c = itemindex + 1))
        print('{a}: Exit store.'.format(a = len(items) + 1))
        ch = Inputs.num(1,len(items) + 1)
        if ch == len(items) + 1:
            print(exittext)
            time.sleep(1)
            return gold, armor, weapon, hp, mhp, xp
        else:
            if gold >= items[ch-1]['price']:
                gold -= items[ch-1]['price']
                if items[ch-1]['type'] == 'st':
                    if weapon < items[ch-1]['mod']:
                        weapon = items[ch-1]['mod']
                    print('Your damage is now {a}!'.format(a = weapon))
                if items[ch-1]['type'] == 'ar':
                    if armor < items[ch-1]['mod']:
                        armor = items[ch-1]['mod']
                    print('Your defence is now {a}!'.format(a = armor))
                if items[ch-1]['type'] == 'hp':
                    hp += items[ch-1]['mod']
                    if hp > mhp:
                        hp = mhp
                    print('You were healed {a}HP!'.format(a = items[ch-1]['mod']))
                if items[ch-1]['type'] == 'mhp':
                    mhp += items[ch-1]['mod']
                    print('Your max HP is now {a}!'.format(a = mhp))
                if items[ch-1]['type'] == 'xp':
                    xp += items[ch-1]['mod']
                    print('Your xp is now {a}!'.format(a = xp))
                items.remove(items[ch-1])
            else:
                print('You can not aford that.')
#store("Hello.",[{'desc':'Wooden sword, 5 damage.', 'price':100,'type':'st','mod':5},{'desc':'Medikit, +10 Maximum health.', 'price':20,'type':'mhp','mod':10},{'desc':'Health potion, +10 Health.', 'price':20,'type':'hp','mod':10}],120, 0, 1, 95,100, "Goodbye.",25,15)
def city():
    #TODO MAKE CITIES
    pass
