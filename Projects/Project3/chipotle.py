# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477
protein_dictionary = {'chicken': 2.5, 'steak': 3.5, 'barbacoa': 3.5, 'carnitas': 3.0, 'veggies': 2.5, '' :  0, 'white': 2.5, 'brown': 3.5, 'black': 2.5, 'pinto': 2.5, TRUE : }
order1 = ('manan', 'holyoke', 'FLAT3', 'chicken', 'white', 'pinto', False, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream')


def get_protein(order1):
    return protein_dictionary[order1[0]]

print(get_protein('steak'))