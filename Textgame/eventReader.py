import os,configReader,random,lootGen,itemGen,time,tresureChest; import textgamebase as base
def noneg(num):
    if num < 0:
        num = 0
    return num
def getEvent(Armor,Weapon,Gold,hp,mhp,level,xp):
    intro, colours, enames, encounters, deathtexts, edeathtexts, enterTexts, exitTexts = configReader.openConfigs()
    alive = True
    #choose random filename
    filenames = next(os.walk('Configfiles/Events'))[2]
    filename = random.choice(filenames)
    with open('Configfiles/Events/{a}'.format(a = filename), 'r') as x:
        #with open('Configfiles/Events/Merchants.txt', 'r') as x: 
        lines = x.readlines()
        lineNum = 1
        lineLen = len(lines)
        targetDepth = 0
        targetNum = 0
        targetLen = 0
        depth = 0
        lens = {}
        tLens = {}
        tCurr = {}
        looking = False
        ignore = False
        inChoice = False
        print(lines[0])
        for num in range(0,len(lines)-1):
            lines[num] = lines[num][:len(lines[num]) - 1]
            if looking == True:
                if lines[lineNum][0:2] == '!c':
                    lines[lineNum]= lines[lineNum][3:]
                    choiceArgs = lines[lineNum].split('|')
                    choiceArgs[len(choiceArgs)-1] = int(choiceArgs[len(choiceArgs)-1][len(choiceArgs[len(choiceArgs)-1])-2:])
                    lens[depth] = choiceargs[len(choiceArgs)-1]
                    depth += 1
                if lines[lineNum][0:2] == '!r':
                    lines[lineNum]= lines[lineNum][3:]
                    choiceArgs = lines[lineNum].split('|')
                    choiceArgs = choiceArgs[0]
                    choice = random.choice(range(0,int(choiceArgs)+1))
                    lens[depth] = choiceArgs[int(choiceArgs)]
                    depth += 1
                if lines[lineNum][0:2] == '!{a}'.format(a = targetNum):
                    inChoice = True
                    looking = False
                    tLens[depth] = targetLen
                    tCurr[depth] = targetNum
            elif ignore == True:
                if lines[lineNum][0:2] == '!e':
                    if tLens[depth] == tCurr[depth]:
                        ignore = False
                        depth -= 1
                    else:
                        tCurr[depth] += 1
            else:
                #Main

                #fighta
                if lines[lineNum][0:2] == '!f':
                    if lines[lineNum][2] == 'r':
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
                        alive, gp, Armor, Weapon, hp = base.fight(hp, mhp, Weapon, Armor, (level * hpmod), (level * hpmod), (level * strmod), noneg(level - armod), ename, encounter, deathtext, edeathtext, {'Gold':lootGold,'Weapon':lootWeapon,'Armor':lootArmor}, False) 
                        Gold += gp
                        xpmod = random.randint(((level + 5) * 2),((level + 10) * 2))
                        xp += xpmod
                        print('You got {a} xp!'.format(a = xpmod))


                        #ELSE
                    else:
                        lines[lineNum] = lines[lineNum][4:]
                        fightArgs = lines[lineNum].split('|')
                        for arg in range(0,4):
                            fightArgs[arg] = int(fightArgs[arg])
                        fightArgs[9] = int(fightArgs[9])
                        fightArgs[8] = fightArgs[8].split(',')
                        fightArgs[8][0] = int(fightArgs[8][0])
                        if fightArgs[8][1] == 'False':
                            fightArgs[8][1] = False     
                        else:
                            fightArgs[8][1] = fightArgs[8][1].split('/')
                            fightArgs[8][1][1] = int(fightArgs[8][1][1])
                            fightArgs[8][1] = {'desc':fightArgs[8][1][0],'mod':fightArgs[8][1][1]+level}
                        if fightArgs[8][2] == 'False':
                            fightArgs[8][2] = False
                        else:
                            fightArgs[8][2] = fightArgs[8][2].split('/')
                            fightArgs[8][2][1] = int(fightArgs[8][2][1])
                            fightArgs[8][2] = {'desc':fightArgs[8][2][0],'mod':fightArgs[8][2][1]+level}
                        alive, gp, Armor, Weapon, hp = base.fight(hp,mhp,Weapon,Armor ,fightArgs[0]*level,fightArgs[1]*level,fightArgs[2]*level,noneg(level-fightArgs[3]),fightArgs[4],fightArgs[5],fightArgs[6],fightArgs[7],{'Gold':fightArgs[8][0]*level,'Weapon':fightArgs[8][1],'Armor':fightArgs[8][2]}, False)
                        Gold += gp
                        xpmod = fightArgs[9]*level
                        xp += xpmod



                #Choice (Get input)
                if lines[lineNum][0:2] == '!c':
                    lines[lineNum]= lines[lineNum][3:]
                    choiceArgs = lines[lineNum].split('|')
                    choiceArgs[len(choiceArgs)-1] = int(choiceArgs[len(choiceArgs)-1][len(choiceArgs[len(choiceArgs)-1])-2:])
                    choice = base.story(choiceArgs[0],choiceArgs[1:len(choiceArgs)-1],1,choiceArgs[len(choiceArgs)-1])
                    lens[depth] = choiceArgs[len(choiceArgs)-1]
                    targetLen = lens[depth]
                    depth += 1
                    targetDepth = depth
                    targetNum = choice
                    looking = True
                    #|text|option_1|2|3|4...|number_of_choices
                if lines[lineNum][0:2] == '!r':
                    lines[lineNum]= lines[lineNum][3:]
                    choiceArgs = lines[lineNum].split('|')
                    choiceArgs = choiceArgs[0]
                    choice = random.choice(range(0,int(choiceArgs)+1))
                    lens[depth] = int(choiceArgs)
                    targetLen = lens[depth]
                    depth += 1
                    targetDepth = depth
                    targetNum = choice
                    looking = True
                
                #Printing
                if lines[lineNum][0:2] == '!p':
                    lines[lineNum] = lines[lineNum][3:]
                    print(lines[lineNum])

                #store(entertext,items, gold, armor, weapon, hp, mhp, exittext, xp, level)
                #or
                #!sf|entertext|exittext|item1::item2::item3...
                #or
                #!st|entertext|exittext|type
                #or
                #!sr
                #{'desc':'Wooden sword, 5 damage.','price':100,'type':'st','mod':5}
                if lines[lineNum][0:2] == '!s':
                    #Fixed
                    if lines[lineNum][2] == 'f':
                        items = []
                        lines[lineNum]= lines[lineNum][4:]
                        storeArgs = lines[lineNum].split('|')
                        stareArgs[2] = storeArgs[2][:len(storeArgs[2])-2]
                        storeArgs[2] = storeArgs[2].split('::')
                        for item in storeArgs[2]:
                            item = item[:len(item)]
                            itemc = item.split('##')
                            items.append({'desc':itemc[0],'price':int(itemc[1]*level),'type':itemc[2],'mod':int(itemc[3])})
                        print(items)
                        Gold, Armor, Weapon, hp, mhp, xp = base.store(storeArgs[0], items, Gold, Armor, Weapon, hp, mhp, storeArgs[1], xp, level)
                        
                    if lines[lineNum][2] == 't':
                        lines[lineNum]= lines[lineNum][4:]
                        storeArgs = lines[lineNum].split('|')
                        items = itemGen.getItemsByType(level,xp,25,Armor,mhp,storeArgs[2][:len(storeArgs[2])-1])
                        Gold, Armor, Weapon, hp, mhp, xp = base.store(storeArgs[0], items, Gold, Armor, Weapon, hp, mhp, storeArgs[1],xp, level)
                    if lines[lineNum][2] == 'r':
                        lines[lineNum]= lines[lineNum][4:]
                        items = itemGen.getItems(level,xp,25,Armor,mhp)
                        Gold, Armor, Weapon, hp, mhp, xp = base.store(random.choice(enterTexts), items, Gold, Armor, Weapon, hp, mhp, random.choice(exitTexts),xp, level)
                    
                #Treasure chest    
                if lines[lineNum][0:2] == '!t':
                    #random
                    if lines[lineNum][2] == 'c':
                        lines[lineNum] = lines[lineNum][4:]
                        chestArgs = lines[lineNum].split('|')
                        Weapon,Armor,hp,mhp,xp,level = tresureChest.get(Weapon,Armor,hp,mhp,xp,level,int(chestArgs[0]),int(chestArgs[1]))
                    #fixed item
                
                if inChoice:
                    if lines[lineNum][0:2] == '!e':
                        if tLens[depth] == tCurr[depth]:
                            inChoice = False
                            depth -= 1
                        else:
                            tCurr[depth] += 1
                            inChoice = False
                            ignore = True
                            
            lineNum += 1
            if alive == False:
                time.sleep(5)
                quit()
        return Armor,Weapon,Gold,hp,mhp,level,xp

