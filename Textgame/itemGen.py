import random, configReader
def getItems(level,xp,LV_UP,Armor):
    weapons, armor = configReader.itemConfig()
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
            if level < 5:
                descMat = 'Wooden'
            elif level < 10:
                descMat = 'Stone'
            elif level < 15:
                descMat = 'Iron'
            elif level < 20:
                descMat = 'Steel'
            elif level < 25:
                descMat = 'Golden'
            elif level < 30:
                descMat = 'Enchanted'
            elif level < 40:
                descMat = 'Diamond-Encrusted'
            else:
                descMat = 'Godblood-Forged'
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
            if level < 5:
                descMat = 'Wooden'
            elif level < 10:
                descMat = 'Stone'
            elif level < 15:
                descMat = 'Iron'
            elif level < 20:
                descMat = 'Steel'
            elif level < 25:
                descMat = 'Golden'
            elif level < 30:
                descMat = 'Enchanted'
            elif level < 40:
                descMat = 'Diamond-Encrusted'
            else:
                descMat = 'Godblood-Forged'
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
            if level < 10:
                mod = 50
                desc = 'Small Health Potion: 50 Health'
            elif level < 20:
                mod = 100
                desc = 'Health Potion: 100 Health'
            elif level < 30:
                mod = 150
                desc = 'Medium Health Potion: 150 Health'
            elif level < 40:
                mod = 200
                desc = 'Large Health Potion: 200 Health'
            elif level < 50:
                mod = 250
                desc = 'HUGE Health Potion: 250 Health'
            else:
                mod = 500
                desc = 'IMPOSSIBLY LARGE Health Potion: 500 Health'
            stat = 'hp'
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
            itemType = random.randint(1,8)
            if itemType == 1 or itemType == 2:
                mod = random.choice([1,1,1,1,1,1,1,1,1,1,2,2,3])
                stat = 'st'
            if itemType == 3 or itemType == 4:
                mod = random.choice([0,0,0,0,0,0,0,0,0,0,1,1,2])
                stat = 'ar'
            if itemType == 5 or itemType == 6:
                mod = random.randint(50,500)
                stat = 'hp'
            if itemType == 7:
                mod = random.randint(level * 1, level * 5)
                stat = 'mhp'
            if itemType == 8:
                mod = random.randint(level * 5, level * 10)
                stat = 'xp'
        items.append({'desc':desc,'price':cost,'type':stat,'mod':mod})
    return items
