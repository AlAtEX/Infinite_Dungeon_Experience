import sys, time, random, os, configReader, Inputs, saveManager, itemGen, lootGen, tresureChest, eventReader; import textgamebase as base; 
alive = True
Armor = 0#0
Weapon = 1 #1
Gold = 0 #0
hp = mhp = 100 #100
quest =  False
level =  1 # 1, DUH!
xp = 0 #0

LV_UP = 25 # ~25 is good
saveQuit = False

VERSION = '0.2 Beta'

def noneg(num):
    if num < 0:
        num = 0
    return num

intro, colours, enames, encounters, deathtexts, edeathtexts, enterTexts, exitTexts = configReader.openConfigs()

'''
        for char in #:
            if char == '#':
                flagPos = #.index('#')
                # = '{a}{b}{c}'.format(a = #[:flagPos], b = #, c = #[flagPos + 1:])
'''

print('Welcome to "The Infinite Dungeon Experience"! {a}'.format(a =  intro))
print(VERSION)

isProperSaveFile = saveManager.preLoad()
if isProperSaveFile:
    print('Save file detected.')
    z,a,b,c,d,e,x,f,g = saveManager.load(True)
    print('Armor:{a}, Weapon:{b}, Gold:{c}, {d}/{e}HP, Level:{f} with {g}/{h} xp'.format(a = a,b=b,c=c,d=d,e=e,f=f,g=g,h=f*LV_UP))
    print('would you like to load it? (If no, then save WILL be deleted.)\n1:Y\n2:N')
    firstChoice = Inputs.num(1,2)
else:
    firstChoice = 3
if firstChoice == 1:
    alive, Armor, Weapon, Gold, hp, mhp, quest, level, xp = saveManager.load(True)
if firstChoice == 2:
    os.remove('Saves/save.sav')
time.sleep(1)



while alive:
    #1,2 = get quest/finish quest, 3,4 = choice/puzzle, 5,6 = fight, 7 = store,
    event = random.randint(3,8)
    if event == 1 or event == 2:
        print('QUEST') 
        if quest == False:
            pass #TODO Get new quest
        else:
            pass #TODO Read quest data and do the next part.
    if event == 3:
        Armor,Weapon,Gold,hp,mhp,level,xp = eventReader.getEvent(Armor,Weapon,Gold,hp,mhp,level,xp)
        time.sleep(1)
    if event == 4 or event == 5 or event == 6:

        #Fights
        saveQuit = False
        #fight(hp, mhp, st, ar, ehp, emhp, est, ear, ename, encounter, deathtext, edeathtext, loot)
        hpmod = random.randint(1,3)
        strmod = random.randint(1,3)
        armod = random.randint(8,10)
        ename = random.choice(enames)
        for char in ename:
            if char == '#':
                flagPos = ename.index('#')
                ename = '{a}{b}{c}'.format(a = ename[:flagPos], b = random.choice(colours) , c = ename[flagPos + 1:])
        encounter = random.choice(encounters)
        for char in encounter:
            if char == '#':
                flagPos = encounter.index('#')
                encounter = '{a}{b}{c}'.format(a = encounter[:flagPos], b = ename , c = encounter[flagPos + 1:])
        deathtext = random.choice(deathtexts)
        for char in deathtext:
            if char == '#':
                flagPos = deathtext.index('#')
                deathtext = '{a}{b}{c}'.format(a = deathtext[:flagPos], b = ename , c = deathtext[flagPos + 1:])
        edeathtext = random.choice(edeathtexts)
        for char in edeathtext:
            if char == '#':
                flagPos = edeathtext.index('#')
                edeathtext = '{a}{b}{c}'.format(a = edeathtext[:flagPos], b = ename, c = edeathtext[flagPos + 1:])
        lootGold = random.randint(level, level + 20)
        weapon = random.choice([False,False,False,False,False,False,False,False,False,True])
        if weapon:
            lootWeapon = lootGen.lootGen(level,'weapon')
        else:
            lootWeapon = False
        armor = random.choice([False,False,False,False,False,False,False,False,False,True])
        if armor:
            lootArmor = lootGen.lootGen(level,'armor')
        else:
            lootArmor = False
        alive, gp, Armor, Weapon, hp = base.fight(hp, mhp, Weapon, Armor, (level * hpmod), (level * hpmod), (level * strmod), noneg(level - armod), ename, encounter, deathtext, edeathtext, {'Gold':lootGold,'Weapon':lootWeapon,'Armor':lootArmor}, True) 
        Gold += gp
        xpmod = random.randint(((level + 5) * 2),(((level + 10) * 2)))
        xp += xpmod
        print('You got {a} xp!'.format(a = xpmod))
    if event == 7 or event == 8:
        saveQuit = True
        #store(entertext, items, gold, armor, weapon, hp, mhp, exittext, xp, level)
        enterExitIndex = random.randint(0,len(enterTexts) - 1)
        enterText = enterTexts[enterExitIndex]
        exitText = exitTexts[enterExitIndex]
        
        items = itemGen.getItems(level,xp,LV_UP,Armor,mhp)
        
        Gold, Armor, Weapon, hp, mhp, xp = base.store(enterText, items, Gold, Armor, Weapon, hp, mhp, exitText, xp, level)
    
    lvup = level * LV_UP
    if alive:
        print ("You are level {a}, and have {b}/{c}xp.".format(a = level, b = xp, c  = lvup))
        if xp >= lvup:
            level  += 1
            xp -= lvup
            print("You leveled up to level {a}!".format(a = level))
            mhp += 10
            hp = mhp
            print("You have {a}/{b}HP and do {c} damage with {d} armor.".format(a=hp,b=mhp,c=Weapon,d=Armor))
            saveQuit = True
        if saveQuit:
            print('Would you like to save and quit?\n1:Y\n2:N')
            saveAndQuit = Inputs.num(1,2)
            if saveAndQuit == 1:
                saveManager.Save(alive,Armor,Weapon,Gold,hp,mhp,quest,level,xp)
                quit()
    else:
        os.remove('Saves/save.txt')
    time.sleep(1)
