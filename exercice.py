#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1) Vérifier si le nombre de caractères d’une chaîne de caractères est pair
2) Supprimer le 3ème caractère d’une chaîne de caractères
3) Remplacer un caractère d’une chaîne de caractère par un autre
4) Renvoyer le nombre d’occurrences d’un caractère dans une chaîne de caractères, sans utiliser de fonctions avancées
5) Rechercher le nombre de mots dans une phrase donnée
"""


def is_even_len(string: str) -> bool:
    if len(string) % 2:
        return True

    return False


def remove_third_char(string: str) -> str:
    new_string = string[:2] + string[3:]

    return new_string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    for i in range(len(string)):
        if string[i] == old_char:
            string = string[:i] + new_char + string[i+1:]

    return string

def get_number_of_char(string: str, char: str) -> int:
    count = 0
    for c in string:
        if c == char:
            count += 1

    return count

def get_number_of_words(sentence: str, word: str) -> int:
    count = 0
    sentence = sentence.split()
    for w in sentence:
        if w == word:
            count += 1

    return count


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
