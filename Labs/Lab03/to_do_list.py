# Author: Eduardo Suarez Del Valle
# Email: esuarez@umass.edu
# Spire ID: 34750477



to_do_list = []

def add_task(_list1, _string_object):
    _list1.append(_string_object)
    x = len(_list1)
    return f"Task successfully added. {x} tasks remaining."

def delete_task(_list2, _delete_task):
    _list2.remove(_delete_task)
    x = len(_list2)
    return f"Task successfully deleted. {x} tasks remaining."


def move_task(_list3, from_index, to_index):
    task = _list3[from_index]
    _list3.pop(from_index)
    _list3.insert(to_index, task)
    return f"Task '{task}' successfully moved to index {to_index}"




