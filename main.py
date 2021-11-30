import requests
import itertools


def perm(raw: str):
    all_perms = set(itertools.permutations(raw))
    print('To slowo mozna spermutawac na ', len(all_perms), ' sposobow')
    if input('Czy chcesz zobaczyc wszystkie sposoby? ').lower() == 'y':
        print(list(set(all_perms)))
    if input('Czy chcesz zobaczyc wszystkie sensowne permutacje?').lower() == 'y':
        sens(all_perms)


def check(query):
    website = requests.get(f'https://sjp.pwn.pl/slowniki/{query}.html')
    if "Nie znaleziono żadnych wyników wyszukiwania dla:" in website.text:
        return False
    else:
        return True


def sens(every):
    for one in every:
        if check(''.join(one)):
            print(''.join(one))


if __name__ == "__main__":
    word: str = input('Podaj slowo ktore chcesz spermutowac: ')
    perm(word)
    pass
