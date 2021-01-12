print('enter une chaine de caractere')
chaine = input() 
chainePaire=''
chaineImppaire=''
for i in range(len(chaine)):
    if(i%2==0):
        chainePaire=chainePaire+chaine[i]
    else:
        chaineImppaire=chaineImppaire+chaine[i]

print('les les caractére a l\'indix paire sont les suivant',chainePaire)
print('les les caractéres a l\'indix impaire sont les suivant',chaineImppaire)
print('les la combinaison est',chainePaire+chaineImppaire)
