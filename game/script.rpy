# Vous pouvez placer le script de votre jeu dans ce fichier.


# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
# Déclarez les personnages utilisés dans le jeu.

define mc = Character("", kind=nvl)
define narrator = nvl_narrator
init:

    image rain:
        animation
        "rain1.png"
        0.1
        "rain3.png"
        0.1
        "rain2.png"
        0.1
        repeat
        
    image lightning:
        animation
        choice:        #weight of choice is 1
            "lightning.png"
            alpha  0.0
            0.5                 # show nothing for 0.5 seconds
        
        choice 0.1:   #weight of choice is 0.1
            "lightning.png"
            alpha  0.0
            linear 0.3 alpha  1.0
            linear 0.3 alpha  0.0
            
        choice 0.1:
            "lightning.png"
            alpha  0.0
            linear 0.3 alpha  1.0
            linear 0.3 alpha  0.0
            xzoom -1
            
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
    show lightning
    with fade

    """
    Autour de moi, il n’y avait rien. C’était un paysage immense, mais avec rien à l’horizon excepté une plaine entourée par une chaîne montagneuse.

    Peut-être y’avait-il autre chose, mais mes yeux étaient incapables de distinguer quoi que ce soit. 

    {clear}
    
    Je ne suis pas sûr d’avoir même cherché à regarder autour de moi.

    Toutefois, je jurerai qu’il y’avait plusieurs éclairs qui frappaient les montagnes proches de nous. Je ne les voyais pas, mais je les entendais comme s’ils atterrissaient à côté de mes oreilles, eux et leurs bruits assourdissants.

    {clear}

    Maintenant que j’y repense, mon corps était totalement engourdi, incapable de bouger ni même de faire quoi que ce soit.

    {clear}
  
    Cependant, je me souviens d’une chose, les premiers mots que l’on m’a adressés.
  
    « Hé, petit, qu’est-ce que tu fais là ? »
   
    C’était une voix d’homme.

    {clear}
  
    Je ne me rendais pas compte de sa taille, mais il avait l’air très imposant.
  
    Après, quel enfant ne trouverait pas imposant un soldat en armure sur un cheval.

    {clear}
   
    Alors que je levais la tête pour voir d’où provenait la voix, je pouvais voir qu’il venait de descendre de son cheval.
   
    Un coup d’œil m’a permis de remarquer qu’une personne portant la même armure se trouvait à côté de moi, il s’agissait probablement de la personne qui m’avait mis la serviette sur la tête.
  
    {clear}

    Alors que la pluie continuait à battre et la foudre continuait à gronder, je regardait l’homme devant moi qui me paraissait être un géant.
   
    Bouche-bée, je n’arrivait pas à dire quoi que ce soit, avais-je seulement la volonté de dire quoi que ce soit ?
   
    {clear}

    L’homme se rapprocha alors de moi et dit
   
    « Hé, petit, qu’est-ce que tu fais là ? Et comment tu t’appel ? »
  
    Aucun son ne sortit de ma bouche grande ouverte.
   
    Il posa se tourna alors vers son collègue à mes côtés et dit
  
    « On dirait qu’il a les cordes vocales brisées, le camp est un peu loin mais il va falloir le ramener avec nous, on cherchera plus tard son identité. »
  
    Le soldat acquiesça.
   
    « Bien ! »

    {clear}
   
    L’homme se tourna alors vers d’autres personnes derrière lui, toutes en armure et à cheval.
   
    « ON A UN ENFANT QUI A L’AIR D’AVOIR DOUZE OU TREIZE ANS SUR LES BRAS, ON VA LE RAMENER AVEC NOUS CAMP, JE LE PRENDS AVEC MOI SUR MON CHEVAL. ON VA ADOPTER LA FORMATION C-38 ! »
   
    Je ne sais pas si c’est la météo ou bien le contexte militaire qui le forçait à parler aussi fort, mais je me souviens bien de ce moment.
   
    Il m’enroula alors dans ce qui semblait être un drap, me colla entre lui et le cheval et commença à galoper.
    
    Le visage collé à l’armure de ce qui semblait être le supérieur de ces soldat faisant que, je ne pouvait rien voir, donc je ne savais pas comment cette formation « C-38 » était sensée s’articuler, mais la finalité était là ils finirent par m’amener à leur camp militaire.
    
    {clear}
    
    Là-bas on a fini par me poser tout un tas de questions, incapable de parler je répondait en hochant la tête de haut en bas ou de droite à gauche.
    
    Mais ne me souvenant d’absolument rien, c’était la seconde option qui était le plus souvent privilégié.
    
    {clear}

    Chercher à me souvenir de quelque chose était comme se confronter à un mur, peu importe comment j’essayais, la méthode utilisée rien n’y faisait. 
    
    Comme si l’entièreté de mon existence avant que l’on me trouve avait été emporté par un trou noir.
    
    Après cela, les soldats qui m’ont retrouvé ont fait pas mal de recherches afin que de trouver mes origines.

    Il n’y avait absolument rien à l’endroit où ils m’ont retrouvé, ni calèches, ni vêtements, ni informations utilisables.
    
    {clear}
    
    Sotilas, j’ai découvert quelques temps après qu’il s’agissait du nom du soldat qui m’a trouvé, a interroger les villages les plus proches, mais rien.
    
    Il a alors pensé qu’un convoi a pu se faire attaquer par des bandits, et que j’aurai réussi à trouver un moyen de m’enfuir, mais aucune information dans se sens ni avis de disparition de qui que ce soit n’a été émis une durant la semaine précédant ni durant la semaine suivant.
    
    {clear}

    Ils ont cherché, cherché, cherché et encore cherché, mais rien ni fus. 
    
    C’est comme si je n’avais jamais existé. 
    
    La thèse qui a finalement été retenu c’est que j’ai été abandonné dans une forêt non loin par ma famille qui m’aurait abandonnée pour une quelconque raison.
    
    {clear}

    Quand j’ai découvert ça… je n’ai pas pu pleurer, je n’ai même pas ressenti quoi que ce soit. 
    
    Après tout, dans mon esprit, le mot « famille » n’était associé à rien.
    
    Ni visage, ni personnes, ni concept.
    
    {clear}

    """


    
return

