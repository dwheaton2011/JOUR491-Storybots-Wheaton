#assignment number 3, using randomness 



import random    
names = ["Harvey Perlman","Bo Pelini","Dave Heineman","Jon Bruning", "Mike Foley", "John", "Deb Fischer","Lee Terry","Adrian Smith","Jeff Fortenberry"]

verbs = ["cancelled school","lost","ignored a scandal","called plebians racoons","attacked his sister","lied","farmland","took dirty money","cursed","voted"]
    
for verb in verbs:
for name in names: 
    print random.choice(names),"was very naughty, they" ,random.choice(verbs), "today." 
        
