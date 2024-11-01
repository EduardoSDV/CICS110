# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477


def count_words(_tuple):
    _dict = {}
    for value in _tuple:
        if value in _dict:
            _dict[value] += 1
        else:
            _dict[value] = 1
    return _dict

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))




def average_prices(commodities):
    total_prices = {}
    counts = {}

    for name, price in commodities:
        if name in total_prices:
            total_prices[name] += price
        else:
            total_prices[name] = price
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1

    average_price_dict = {name: total_prices[name] / counts[name] for name in total_prices}

    return average_price_dict

prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
print(average_prices(prices))

def count_bigrams(t):
    bigrams_dict = dict()
    pass



