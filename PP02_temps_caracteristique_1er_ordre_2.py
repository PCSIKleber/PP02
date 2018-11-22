# pour l'import des donnees
import numpy as np
# La lecture proprement dite
t1,u1,t2,u2 = np.loadtxt('regime_transi2.txt',unpack=True)

# A vous de trouver une caracterisation assez solide pour determiner la 
# position (=indice dans la liste) du debut du regime transitoire dans les 
# listes des tensions.

def debut_transitoire(u):
    return 0 # Peu probable, bien sur...


# Appliquez la fonction precedemment definie pour trouver lesdits
# indices pour les deux enregistrements

i1 = 'Resultat pour (t1,u1)'
i2 = 'Resultat pour (t2,u2)'

# On affiche les resultats
print(i1,i2)
