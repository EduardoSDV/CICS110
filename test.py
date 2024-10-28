def longest_word(_list):
    if not _list:
        return None
    longest = ''
    for el in _list:
        if len(el) > len(longest):
            longest = el
    return longest

def remove_duplicates(duplicates):
    empty_list = []
    for el in duplicates:
        if el not in empty_list:
            empty_list.append(el)

    return empty_list


def sum_of_even_numbers(integers):
    sum = 0
    if not integers:
        return 0
    for number in integers:
        if number % 2 == 0:
            sum += number
    return sum

print(sum_of_even_numbers([1,2,3,4,5,6]))







