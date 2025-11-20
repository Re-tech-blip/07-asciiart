#### Imports et définition des variables globales
""" Module principal pour ASCII Art.
Contient des fonctions pour encoder et afficher des chaînes de caractères."""
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1

    for c in s[1:]:
        if c == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = c
            count = 1
    result.append((current_char, count))  # ajout du dernier groupe

    return result


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument
    selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    # compter le nombre de caractères identiques au début
    count = 1
    while count < len(s) and s[count] == s[0]:
        count += 1
    # encodage du premier bloc
    first_tuple = [(s[0], count)]
    # appel récursif sur le reste
    return first_tuple + artcode_r(s[count:])


#### Fonction principale


def main():
    """Effectue des tests du modules"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
