# Vous pouvez placer le script de votre jeu dans ce fichier.


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
# Déclarez les personnages utilisés dans le jeu.

define mc = Character("", kind=nvl)
define narrator = nvl_narrator
init:
    image rain:
        "rain 1.png"
        0.1
        "rain 3.png"
        0.1
        "rain 2.png"
        0.1
        repeat

# Le jeu commence ici
label start:    
    scene black

    narrator """

    Quel est notre premier souvenir ?

    On raconte qu'il est pratiquement impossible de se souvenir de quoi que ce soit avant l’âge de 3 ans. 
    \nLe cerveau humain est fait de sorte que jusqu’à cet âge-là, il soit en pleine reconstruction limitant la capacité 
    à avoir des souvenirs antérieurs à cette période.
    \n

    Dans ce cas-là, quel doit être notre premier souvenir ?


    {clear}

    Est-ce que ça doit être le moment exact où notre cerveau a fini de se reconstruire ? 



    Ou bien, un moment tout à fait aléatoire après cela ? 

    {clear}

    Le souvenir doit-il être marquant, ou bien lointain ? Est-il flou ou bien net ?

    {clear}

    D’ailleurs, je suis persuadé que cette histoire de 3 ans n’est pas une règle absolue.
    \n\nIl doit y avoir, dans ce monde, une personne qui se souvient du jour de sa naissance.

    {clear}

    Non.



    Peut-elle que cette personne ne vit-elle plus dans ce monde.\n

    {clear}

    Je suis sur qu’en cherchant bien, il devrait être possible de trouver une revue, un journal, un grimoire ou bien une vieille légende de \nquelqu’un capable de se souvenir du jour de sa naissance.

    \nCe serait cocasse, je pense que beaucoup de monde seraient curieux d’avoir ce type de souvenir. 

    \nÇa pourrai être un sujet de conversation marrant j’imagine.

    \n\n« Tu sais, tu sais, j’ai des souvenirs du jour de ma naissance ! »
    \n\n« Naaaaaaan, tu mens ! »
    \n\n« Si je te promets, je m’en souviens parfaitement. »


    \n\nQuelque chose dans le genre.

    {clear}

    Ce serait drôle, en effet.

    \nPavané devant ses connaissances, en rire et s’en remémorer avec nostalgie, j’imagine que beaucoup de monde voudraient bien.

    \n
    \n
    \nMais ce serait triste aussi.

    {clear}

    Ce serait triste d’avoir à se souvenir de tout depuis sa naissance.

    {clear}

    Les bons moments arriveraient-ils à compenser les mauvais ?\n

    Pour nous protéger, on arrive à supprimer inconsciemment ce qui nous fait le plus souffrir.\n

    Mais si nous…\n
    \n
    \n


    Mais si l’homme a évolué de sorte à développer cette capacité, est-ce que ça ne serait pas pour se protéger?

    {clear}

    On se souvient pour apprendre, on assimile les erreurs du passé pour ne plus les reproduire, et en ne les reproduisant pas on fait un pas en avant.\n

    Si l’on fait une expérience, et que l’on place un enfant face à des flammes ardentes, et qu’il plonge sa main dedans. \nQue se passera-t-il ? \n

    Dès que le cerveau recevra la douleur, il ordonnera au bras de se retirer.\n

    L’enfant pleurera, il en gardera peut-être même une cicatrice, mais cette douleur sera importante. \nCette douleur sera transformée en information.\n\n
    « Le feu cause de la douleur. »

    {clear}

    Plusieurs années plus tard, alors même qu’il en gardera une cicatrice, il ne se souviendra plus de la douleur perçue à ce moment-là. 

    Il aura le vague souvenir d’avoir eu mal, mais ce sera à mille lieux de la réalité.
    Je pense que l’homme a évolué de cette manière là pour se protéger.
    \n

    Oublier la douleur, garder les informations essentielles tout cela, pour continuer à avancer.\n

    {clear}

    C’est pour ça que ce serait triste.\n\n

    Quelqu’un qui se souviendrait constamment de la douleur de ces flammes, ne serait-elle pas à plaindre ?\n

    {clear}

    Si notre cerveau… Non. 

    Si nous nous souvenons d’absolument tout du jour de notre naissance, à celui de notre mort, comment pourrions nous oublier la douleur lors des moments de joies ? 
    \n

    Ces moments-là ne seraient-ils pas entachés à leur tour ?

    {clear}

    Cela est évidemment si l’on prend en compte l’hypothèse suivante :

    La personne qui se souviens du jour de sa naissance, se souviens également de tous les autres jours qu’elle a vécu.
    \n

    Evidemment qu’il s’agit d’un postulat biaisé.

    Mais il devrait exister au moins une personne comme ça, non ?

    {clear}

    J’espère juste que cette personne n’a pas existé.


    Ca pourrait paraitre ridicule, mais j’espère sincèrement que cette personne n’est pas encore née, et si c’est le cas, depuis pas très longtemps.

    {clear}

    J’aimerai pouvoir la rencontrer.

    J’aimerai pouvoir lui parler.

    J’aimerai pouvoir l’écouter.

    J’aimerai pouvoir la plaindre.

    J’aimerai pouvoir lui demander si elle va bien.

    J’aimerai pouvoir lui trouver des mots pour décrire son angoisse et sa solitude.
    \n

    Cette angoisse de ne pas pouvoir oublier la douleur.

    Cette solitude de ne pas pouvoir être comprise.


        {clear}

    Pourquoi est-ce que je parle de tout ça ?

    Si existe quelqu’un capable de pouvoir se souvenir du jour de sa naissance, n’est-il pas logique que quelqu’un soit incapable de se souvenir du moindre souvenir ?

    {clear}

    L’ombre se cache derrière la lumière tandis qu’elle amplifie elle-même l’ombre.

    Le fort ne peut être fort que si le mot « faible » existe.

    Le grand et le petit.

    Le riche et le pauvre.

    Le haut et le bas.

    Le bien et le mal.
    \n

    Si quelqu’un est capable de se souvenir de tout, sa Némésis existe forcément.

    {clear}

    Pour ma part, je n’ai pas de premier souvenir.

    {clear}

    Enfin, dire cela n’est pas tout à fait vrai quand même, j’ai ce que je pourrai appeler « un lointain souvenir ».

    Non.

    Même dire cela n’est pas suffisant pour décrire réellement ma situation.
    \n
    \n

    « Je ne me souviens de rien avant mes treize ans ».

    {clear}

    Oui, c’est bien plus proche de la réalité.
    
    {clear}
 
    """

    jump flashback

return


label flashback:
    scene black 
    with fade
    play music rain  fadein 0.5 loop
    

    """

    Je me souviens de la pluie battante du jour où l’on m’a retrouvé.
    J’étais nu…
    En fait, non. Je ne me souviens pas avoir été nu, au moment dont je me souviens, j’avais déjà une serviette sur moi afin de me protéger de la pluie.
    Mais à part cela, j’étais nu.

    {clear}

    """
    scene bg mountains
    show rain
    with fade

    """
    Autour de moi, il n’y avait rien. C’était un paysage immense, mais avec rien à l’horizon excepté une plaine entourée par une chaîne montagneuse.
    Peut-être y’avait-il autre chose, mais mes yeux étaient incapables de distinguer quoi que ce soit. Je ne suis pas sûr d’avoir même cherché à regarder autour de moi.
    Toutefois, je jurerai qu’il y’avait plusieurs éclairs qui frappaient les montagnes proches de nous. Je ne les voyais pas, mais je les entendais comme s’ils atterrissaient à côté de mes oreilles, eux et leurs bruits assourdissants.

    
    """


    
return

