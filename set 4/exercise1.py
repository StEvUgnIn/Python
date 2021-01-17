#!/usr/bin/env python
"""
a)	Retourne le répertoire de travail actuel
b)	Exécutez la commande mkdir dans le shell du système.
c)	Change le répertoire de travail actuel
d)	copier un fichier
e)	déplacer le fichier
f)	Que renvoie cette commande: glob.glob ('*. py'). (Utiliser : import glob).
"""
import glob, os

os.system('mkdir dossier')
os.chdir('dossier')
os.system('copy ../exercise1.py .')
os.system('move ./exercise1.py ..')
os.chdir('..')
glob.glob ('*.py')
