import  configReader,random
def lootGen(level,t):
    weapons, armor, weaponMats, armorMats, potionSizes = configReader.itemConfigs()
    if t == 'weapon':
        itemType = 1
    if t == 'armor':
        itemType = 3
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
    item = {'desc':desc,'mod':mod,'type':stat}
    return item
