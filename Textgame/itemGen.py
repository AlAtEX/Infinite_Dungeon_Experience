import random, configReader
def tresureGen(level,mi,ma,mhp):
    num = random.randint(mi,ma)
    weapons, armor, weaponMats, armorMats, potionSizes = configReader.itemConfigs()
    itemList = []
    for item in range(0,num):
        itemType = random.randint(1,8)
        if itemType == 1 or itemType == 2:
            #weapon
            mod = random.choice([1,1,1,1,1,1,1,1,1,1,2,2,3])
            #Material
            found = False
            for mat in weaponMats:
                try:
                    if level < mat[0] and found == False:
                        descMat = mat[1]
                        found = True
                except:
                    if found == False:
                        descMat = mat[1]
            #Prefix
            if mod == 2:
                descPre = 'Rare '
            elif mod == 3:
                descPre = 'Ledgendary '
            else: 
                descPre = ''
            #Type
            descType = random.choice(weapons)
            mod += level
            desc = descPre +''+ descMat +' '+ descType +': '+ str(mod) +' Damage.'
            stat = 'st'
        if itemType == 3 or itemType == 4:
            #Armor
            mod = random.choice([0,0,0,0,0,0,0,0,0,0,1,1,2])
            #Material
            found = False
            for mat in armorMats:
                try:
                    if level < mat[0] and found == False:
                        descMat = mat[1]
                        found = True
                except:
                    if found == False:
                        descMat = mat[1]
            #Prefix
            if mod == 1:
                descPre = 'Great '
            elif mod == 2:
                descPre = 'Rare '
            else: 
                descPre = ''
            #Type
            descType = random.choice(armor)
            mod += level
            desc = descPre +''+ descMat +' '+ descType +': '+ str(mod) +' Protection.'
            stat = 'ar'
        if itemType == 5 or itemType == 6:
            #Health potion
            mod = int(mhp / 2)
            stat = 'hp'
            found = False
            for size in potionSizes:
                try:
                    if mod < size[0] and found == False:
                        desc1 = size[1]
                        found = True
                except:
                    if found == False:
                        desc1 = size[1]
            desc = desc1 +' '+': {a} HP restored.'.format(a = mod)
        if itemType == 7:
            hc = random.randint(level * 1,level * 5)
            desc = 'Health Increase: {a} Maximum hitpoints'.format(a = hc)
            stat = 'mhp'
            mod = hc
        if itemType == 8:
            x = random.randint(level * 5, level * 10)
            desc = 'Xp potion: {a} Experience'.format(a = x)
            stat = 'xp'
            mod = x
        itemList.append({'desc':desc,'mod':mod,'type':stat})
    return(itemList)
def getItems(level,xp,LV_UP,Armor,mhp):
    weapons, armor, weaponMats, armorMats, potionSizes = configReader.itemConfigs()
    itemNum = random.randint(4,10)
    items = []
    healthCost = random.randint(level*2 + 20, level*2 + 40)
    defaultPrice = random.randint(level*3 + 20, level*3 + 40)
    rndPrice = random.randint(level*3 + 20, level*3 + 40)
    for item in range(1,itemNum):
        
        itemType = random.randint(1,9)
        if itemType == 1 or itemType == 2:
            #weapon
            mod = random.choice([1,1,1,1,1,1,1,1,1,1,2,2,3])
            cost = defaultPrice + mod * 10 + level
            #Material
            found = False
            for mat in weaponMats:
                try:
                    if level < mat[0] and found == False:
                        descMat = mat[1]
                        found = True
                except:
                    if found == False:
                        descMat = mat[1]
            #Prefix
            if mod == 2:
                descPre = 'Rare '
            elif mod == 3:
                descPre = 'Ledgendary '
            else: 
                descPre = ''
            #Type
            descType = random.choice(weapons)
            mod += level
            desc = descPre +''+ descMat +' '+ descType +': '+ str(mod) +' Damage.'
            stat = 'st'
        if itemType == 3 or itemType == 4:
            #Armor
            mod = random.choice([0,0,0,0,0,0,0,0,0,0,1,1,2])
            cost = defaultPrice + mod * 10 + level
            #Material
            found = False
            for mat in armorMats:
                try:
                    if level < mat[0] and found == False:
                        descMat = mat[1]
                        found = True
                except:
                    if found == False:
                        descMat = mat[1]
            #Prefix
            if mod == 1:
                descPre = 'Great '
            elif mod == 2:
                descPre = 'Rare '
            else: 
                descPre = ''
            #Type
            descType = random.choice(armor)
            mod += level
            desc = descPre +''+ descMat +' '+ descType +': '+ str(mod) +' Protection.'
            stat = 'ar'
        if itemType == 5 or itemType == 6:
            #Health potion
            mod = int(mhp / 2)
            stat = 'hp'
            found = False
            for size in potionSizes:
                try:
                    if mod < size[0] and found == False:
                        desc1 = size[1]
                        found = True
                except:
                    if found == False:
                        desc1 = size[1]
            desc = desc1 +' '+': {a} HP restored.'.format(a = mod)
            cost = healthCost
        if itemType == 7:
            hc = random.randint(level * 1,level * 5)
            cost = hc + defaultPrice
            desc = 'Health Increase: {a} Maximum hitpoints'.format(a = hc)
            stat = 'mhp'
            mod = hc
        if itemType == 8:
            x = random.randint(level * 5, level * 10)
            cost = defaultPrice + int(LV_UP/ xp)
            desc = 'Xp potion: {a} Experience'.format(a = x)
            stat = 'xp'
            mod = x
        if itemType == 9:
            desc = 'Random Box: random item'
            cost = rndPrice
            
        items.append({'desc':desc,'price':cost,'type':stat,'mod':mod})
    return items

def getItemsByType(level,xp,LV_UP,Armor,mhp,kind):
    LV_UP = 25
    weapons, armor, weaponMats, armorMats, potionSizes = configReader.itemConfigs()
    itemNum = random.randint(4,10)
    items = []
    healthCost = random.randint(level*2 + 20, level*2 + 40)
    defaultPrice = random.randint(level*3 + 20, level*3 + 40)
    rndPrice = random.randint(level*3 + 20, level*3 + 40)
    for item in range(1,itemNum):
        if kind == 'weapon':
            itemType = 1
        if kind == 'armor':
            itemType = 3
        if kind == 'healthPotion':
            itemType = 5
        if kind == 'healthMax':
            itemType = 7
        if kind == 'xp':
            itemType = 8
        if kind == 'randomBox':
            itemType = 9
        if itemType == 1 or itemType == 2:
            #weapon
            mod = random.choice([1,1,1,1,1,1,1,1,1,1,2,2,3])
            cost = defaultPrice + mod * 10 + level
            #Material
            found = False
            for mat in weaponMats:
                try:
                    if level < mat[0] and found == False:
                        descMat = mat[1]
                        found = True
                except:
                    if found == False:
                        descMat = mat[1]
            #Prefix
            if mod == 2:
                descPre = 'Rare '
            elif mod == 3:
                descPre = 'Ledgendary '
            else: 
                descPre = ''
            #Type
            descType = random.choice(weapons)
            mod += level
            desc = descPre +''+ descMat +' '+ descType +': '+ str(mod) +' Damage.'
            stat = 'st'
        if itemType == 3 or itemType == 4:
            #Armor
            mod = random.choice([0,0,0,0,0,0,0,0,0,0,1,1,2])
            cost = defaultPrice + mod * 10 + level
            #Material
            found = False
            for mat in armorMats:
                try:
                    if level < mat[0] and found == False:
                        descMat = mat[1]
                        found = True
                except:
                    if found == False:
                        descMat = mat[1]
            #Prefix
            if mod == 1:
                descPre = 'Great '
            elif mod == 2:
                descPre = 'Rare '
            else: 
                descPre = ''
            #Type
            descType = random.choice(armor)
            mod += level
            desc = descPre +''+ descMat +' '+ descType +': '+ str(mod) +' Protection.'
            stat = 'ar'
        if itemType == 5 or itemType == 6:
            #Health potion
            mod = int(mhp / 2)
            stat = 'hp'
            found = False
            for size in potionSizes:
                try:
                    if mod < size[0] and found == False:
                        desc1 = size[1]
                        found = True
                except:
                    if found == False:
                        desc1 = size[1]
            desc = desc1 +' '+': {a} HP restored.'.format(a = mod)
            cost = healthCost
        if itemType == 7:
            hc = random.randint(level * 1,level * 5)
            cost = hc + defaultPrice
            desc = 'Health Increase: {a} Maximum hitpoints'.format(a = hc)
            stat = 'mhp'
            mod = hc
        if itemType == 8:
            x = random.randint(level * 5, level * 10)
            if xp == 0:
                cost = defaultPrice
            else:
                cost = defaultPrice + int(LV_UP/ xp)
            desc = 'Xp potion: {a} Experience'.format(a = x)
            stat = 'xp'
            mod = x
        if itemType == 9:
            desc = 'Random Box: random item'
            cost = rndPrice
            
        items.append({'desc':desc,'price':cost,'type':stat,'mod':mod})
    return items

