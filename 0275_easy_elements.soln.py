'''
The inhabitants of the planet Splurth are building their own periodic table of
the elements. Just like Earth's periodic table has a chemical symbol for each
element (H for Hydrogen, Li for Lithium, etc.), so does Splurth's. However,
their chemical symbols must follow certain rules:
* All chemical symbols must be exactly two letters, so B is not a valid
  symbol for Boron.
* Both letters in the symbol must appear in the element name, but the first
  letter of the element name does not necessarily need to appear in the symbol.
  So Hg is not valid for Mercury, but Cy is.
* The two letters must appear in order in the element name. So Vr is valid
  for Silver, but Rv is not. To be clear, both Ma and Am are valid for
  Magnesium, because there is both an a that appears after an m, and an m
  that appears after an a.
* If the two letters in the symbol are the same, it must appear twice in
  the element name. So Nn is valid for Xenon, but Xx and Oo are not.

As a member of the Splurth Council of Atoms and Atom-Related Paraphernalia,
you must determine whether a proposed chemical symbol fits these rules.
'''

'''
Write a function that, given two strings, one an element name and one a
proposed symbol for that element, determines whether the symbol follows the
rules.
The symbol will have exactly two letters. Both element name and symbol will
contain only the letters a-z. Both the element name and the symbol will have
their first letter capitalized, with the rest lowercase. (If you find that too
challenging, it's okay to instead assume that both will be completely lowercase)
'''

def reddit(element, symbol):

    # version 0 -----------------------------------
    # simple check for length
    # doesn't really do much else, so won't solve this problem

    # if len(symbol) != 2:
    #     return False
    # return True

    # version 1 ----------------------------------
    # simple check to see if the letters are present
    #     but does not really worry about order, etc...

    # for letter in symbol.lower():
    #     if letter not in element.lower():
    #         return False
    # return True
    #
    #
    # # version 2 -----------------------------------
    # This version determines if the characters are present in the symbol
    #     as well as determines whether the symbols are in the right order
    #
    # element = element.lower()
    # symbol = symbol.lower()
    #
    # currSymLtr = 0
    #
    # for letters in element:
    #     if letters == symbol[currSymLtr]:
    #         currSymLtr += 1
    #     if currSymLtr > 1:
    #         return True
    # return False

    #
    #
    #
    # # version 3 -----------------------------------
    # This checks for order and for the presence of the
    #     correct letters.

    # letter1, letter2 = symbol.lower()
    # element = element.lower()
    # for letter in element:
    #     if letter == letter1:
    #         location = element.index(letter) + 1
    #         remaining_element = element[location:]
    #         for letter in remaining_element:
    #             if letter == letter2:
    #                 return True
    # return False

    # # version 4 -----------------------------------
    #
    # letter1, letter2 = symbol.lower()
    # element = element.lower()
    #
    # try:
    #     return letter2 in element[element.index(letter1) + 1:]
    # except ValueError:
    #     return False
    #
    # # version 5 -----------------------------------
    # This solution goes through the steps of creating all possible
    #     ordered combinations of letters in the element name and then
    #     checking to see if the symbol is present.

    # from itertools import combinations
    #
    # combos = combinations(element.lower(), 2)
    # combos = {i + j for i, j in combos}
    # if symbol.lower() in combos:
    #     return True
    # return False
    #

    # # version 6 -----------------------------------
    # This solution uses the magic that is regex to help
    #     not only determine if the characters are present in the
    #    element, but if they are in the right order

    # import re
    #
    # try:
    #     pattern = re.compile(r'{}\w*{}'.format(*symbol), re.I)
    #     return bool(pattern.search(element))
    # except ValueError:
    #     return False



if __name__ =='__main__':
    assert reddit('Spenglerium', 'Ee') == True
    assert reddit('Zeddemorium', 'Zr') == True
    assert reddit('Venkmine', 'Kn') == True
    assert reddit('Stantzon', 'Zt') == False
    assert reddit('Melintzum', 'Nn') == False
    assert reddit('Tullium', 'Ty') == False
    print('All tests ran successfully')
