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
    # your code goes here...





if __name__ =='__main__':
    assert reddit('Spenglerium', 'Ee') == True
    assert reddit('Zeddemorium', 'Zr') == True
    assert reddit('Venkmine', 'Kn') == True
    assert reddit('Stantzon', 'Zt') == False
    assert reddit('Melintzum', 'Nn') == False
    assert reddit('Tullium', 'Ty') == False
    print('All tests ran successfully')
