# **VA-11 Hall-A French Translation**
### Préambule
Ceci est un patch intégrant la traduction française Non-Officielle du jeu "VA-11 Hall-A : VA-11 Hall-A: Cyberpunk Bartender Action" par Sukeban Games.

Une partie de la traduction est issue de la traduction qui devait être l'officielle, fournie par Kazuhiro de l’Équipe Mirai et dans un second temps par Gordon Frenchman de l’équipe de traduction officielle.
Également, notez que la publication de cette traduction n'a été approuvé ni par les développeurs du jeu, ni par l'éditeur.

Bien qu'une partie de la traduction soit issue du "leak" de la version qui devait être la version officielle, notez qu'une bonne partie de la traduction n'en est pas issue, a été retraduite ou reformulée affin de rester harmonieux avec notre vision de l'adaptation.

Cette version de la traduction et sa distribution ne bénéficient pas d'une quelconque bénédiction des ayants droits.

La partie "Non-Officielle" de la traduction représente tout de même un travail conséquent et est protégée par le droit d'auteur. CC BY-NC-SA 4.0 (voir [LICENSE.MD](https://github.com/LosDrakakos/VA-11-Hall-A-French-Translation?tab=License-1-ov-file) pour les détails, mais en gros vous faites ce que vous voulez avec tant que : tout le monde est crédité, que cela reste non commercial, et que toutes les oeuvres dérivées de la traduction sont distribuées dans les mêmes conditions.)
Cette traduction est disponible gratuitement sur le site [https://va11-fr.drakakorp.eu](https://va11-fr.drakakorp.eu) ou ici dans l'onglet [Releases](https://github.com/LosDrakakos/VA-11-Hall-A-French-Translation/releases)

### Ce qui a été fait

   - Les dialogues du bar (Traduits par l'équipe de Gordon Frenchman ainsi que The Drakakis, Shikanata et Shushurocket. Relus, harmonisés et intégrés par The Drakakis, Shikanata et Shushurocket )
   - Les monologues de Jill par TheDrakakis
   - Les "dialogues" avec Fore par TheDrakakis
   - Une grande partie de l'interface par TheDrakakis
   - L'autre partie de l'interface par Shushurocket
   - Les recettes des boissons TheDrakakis
   - Les articles de The Augmented Eye (Traduits par l'équipe de Gordon Frenchman et par TheDrakakis. Relecture + harmonisation + intégration The Drakakis)
   - Les articles de /Danger/U/ (Traduits par l'équipe de Gordon Frenchman. Relecture + harmonisation + intégration The Drakakis)
   - Le blog de Kira *Miki* (Traduits par l'équipe de Gordon Frenchman, relecture + harmonisation + intégration The Drakakis)
   - La trad du prologue (Traduits par l'équipe de Gordon Frenchman, relecture + harmonisation + intégration The Drakakis, Shikanata, Kamy et Shushurocket)
   - Relecture générale par Kamy, Shikanata, Shushurocket, et The Drakakis

### Installer / Utiliser le patch
Ce patch remplace complètement la version anglaise du jeu, pour jouer au jeu en anglais après avoir installé le patch, il vous faudra restaurer les fichiers d'origine (via [steam](https://help.steampowered.com/fr/faqs/view/0C48-FCBD-DA71-93EB) par exemple).

#### Pour Windows
 - Aller dans la section [Releases](https://github.com/LosDrakakos/VA-11-Hall-A-French-Translation/releases) de github ou sur le site [va11-fr](https://va11-fr.drakakorp.eu/index.php?categorie1/patch).
 - Sélectionner et télécharger la version la plus récente du patch pour Windows.
 (PS-Edition est la version pour personnes photosensibles.)
 - Lancer `VA-11_Hall-A_Patch_FR_X.X.X_Windows_setup.exe` ou `VA-11_Hall-A_Patch_FR_X.X.X_Windows_PS-Edition_setup.exe` selon l’édition choisie.
 - Suivre les instructions en faisant particulièrement attention au chemin d'installation qui doit pointer vers le repertoire comprenant votre jeu.
 - Lancer le jeu, une fois sur le menu principal, la ligne de credit/copyright doit comporter une mention additionnelle relative au Patch Français.

#### Pour Linux
 - Aller dans la section [Releases](https://github.com/LosDrakakos/VA-11-Hall-A-French-Translation/releases) de github ou sur le site [va11-fr](https://va11-fr.drakakorp.eu/index.php?categorie1/patch).
 - Sélectionner et télécharger la version la plus récente du patch pour Linux.
 (PS-Edition est la version pour personnes photosensibles.)
 - Décompresser l'archive et en mettre le contenu dans votre repertoire de jeu (avec option d'écrasement du contenu)
 - Lancer le jeu, une fois sur le menu principal, la ligne de credit/copyright doit comporter une mention additionnelle relative au Patch Français.

### Désinstaller le patch
Le plus simple reste de faire une [vérification des fichiers de jeu via steam](https://help.steampowered.com/fr/faqs/view/0C48-FCBD-DA71-93EB) qui réécrira les fichiers que la patch a remplacé.

Le patch remplace :
 - Tous les scripts anglais (dans `scripts/eng` pour Windows, et `assets/scripts/eng` pour Linux)
 - Le `data.win` pour windows et `assets/game.unx` pour Linux (grosse blague : c'est le même fichier pour les deux, juste pas le même nom selon l'OS)

Le patch ajoute :
 - Un fichier `Lisez-moi` a la racine du repertoire du jeu.

### Contribuer
Pour contribuer deux options :
 - Rejoindre le [Discord](https://discord.gg/9yRBZqydKw) et signaler les erreurs dans le chan #les-erreurs (merci de lire la faq avant)
 - Faire une PR sur la branche `update/x.x.x` avec les corrections à apporter.
 (Pour les PR, merci de forker le projet avant. Aucune modifications sur le data.win ne sera acceptée, pour les erreurs situées dans ce fichier, merci de les reporter sur discord vu que les modifications au sein d'un binaire ne sont pas trackable via git. La langue des messages de commits peut être l'Anglais ou le Français.)

### Ce qui reste à faire

   - La correction des erreurs nous ayant échappées
   - La correction des erreurs connues dans les images
   - La version Switch : on a fait une version dépackagée de notre jeu pour pouvoir faire un mod via le layerfs Atmosphere (compatible switch moddées et émulateurs), c'est juste que la structure du texte et du data.win est un peu différente. On sait comment faire techniquement, cela dit on a un peu la flemme d'intégrer la traduction dedans parce que c'est fastidieux, mais un jour, promis)
   - La version Vita (on a pas regardé pas dit que ca arrive un jour)

### Crédits et remerciements
Notre équipe / l'équipe de traduction non-officielle / l'équipe de va11-fr (on a pas vraiment de nom en fait) :
 - TheDrakakis
 - Shikanata
 - Shushurocket
 - Kamy

L'équipe de traduction "officielle"/ L'équipe de Gordon Frenchman,
 - Benjamin "Gordon Frenchman/Jcdenton" Doussot
 - Piapiou
 - Odrake
 - Vaea
 - Nävis
 - Keithan
 - Melhoodiey
 - DjDeathrow
 - Kazuhiro

Merci à eux, sans qui notre travail aurait été bien plus long et complexe.

Merci à [SpiritOfRei](https://linktr.ee/spiritofrei) de nous avoir permis d'intégrer son mod incluant des modifications spécifiques pour personnes photosensible. 

Merci également aux utilisateurs du [Discord](https://discord.gg/9yRBZqydKw) nous ayant fait remonter moult erreurs, coquilles, bugs, et retours à la ligne manquants (de manière non exhaustive) :
 - Gamecraft
 - Darcol_Destolle
 - Cow
 - SleepyHuman

Merci à Sukeban pour Va-11 Hall-A, nous attendons la "suite" avec impatience.


