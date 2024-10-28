# Author   : Eduardo Suarez del Valle
# Email    : esuarez@umass.edu
# Spire ID : 34750477

meats = {
    'chicken': 2.5, 'steak': 3.5, 'barbacoa': 3.5, 'carnitas': 3.0, 'veggies': 2.5
}

rice = {
    'white': 2.5, 'brown': 3.5
}

beans = {
    'black': 2.5, 'pinto': 2.5
}

burrito = {
    True: 2.0, False: 0
}

toppings = {
    'veggies': 2.5, 'guacamole': 2.75, 'tomato salsa': 2.5, 'chili corn salsa': 1.75,
    'tomato green chili salsa': 2.0, 'sour cream': 2.5, 'fajita veggies': 2.5,
    'cheese': 2.0, 'queso blanco': 2.75, 'tomatillo green chili salsa': 2.0
}

location_dictionary = {
    'amherst': 15, 'north amherst': 15, 'south amherst': 15, 'hadley': 15,
    'northampton': 30, 'south hadley': 30, 'belchertown': 30, 'sunderland': 30,
    'holyoke': 45, 'greenfield': 45, 'deerfield': 45, 'springfield': 45
}


def get_protein(order):
    return meats.get(order[3], 0)


def get_rice(order):
    return rice.get(order[4], 0)


def get_beans(order):
    return beans.get(order[5], 0)


def get_burrito(order):
    return burrito.get(order[6], 0)


def get_toppings(order):
    total_toppings_price = 0
    protein_choice = order[3]

    for topping in order[7:]:
        if topping in toppings:
            if protein_choice == 'veggies' and (topping == 'guacamole' or topping == 'fajita veggies'):
                continue
            total_toppings_price += toppings[topping]

    return total_toppings_price


def apply_discount(order, total_price):
    discount_code = order[2]

    if discount_code == 'MAGIC':
        return round(total_price * 0.95, 2)
    elif discount_code == 'SUNDAYFUNDAY':
        return round(total_price * 0.90, 2)
    elif discount_code == 'FLAT3':
        return round(total_price - 3, 2)
    else:
        return total_price

def approximate_time(order):
    return location_dictionary.get(order[1], "Unknown location")


def calculate_total_price(order):
    protein_price = get_protein(order)
    rice_price = get_rice(order)
    beans_price = get_beans(order)
    burrito_price = get_burrito(order)
    toppings_price = get_toppings(order)

    total_price = protein_price + rice_price + beans_price + burrito_price + toppings_price
    final_price = apply_discount(order, total_price)

    return final_price


def process_order(order):
    total_price = calculate_total_price(order)
    delivery_time = approximate_time(order)

    print(f"Total price: {total_price}")
    print(f"Estimated delivery time: {delivery_time} minutes")


def generate_invoice(order):
    customer_name = order[0]
    protein_price = get_protein(order)
    rice_price = get_rice(order)
    beans_price = get_beans(order)
    burrito_price = get_burrito(order)
    toppings_price = get_toppings(order)
    discount_code = order[2]

    subtotal = protein_price + rice_price + beans_price + burrito_price + toppings_price
    final_price = apply_discount(order, subtotal)
    money_saved = round(subtotal - final_price, 2)

    delivery_time = approximate_time(order)

    burrito_choice = "Yes" if order[6] else "No"

    topping_list = ', '.join(order[7:])

    print(f"Welcome to Chipotle Mexican Grill Hadley, {customer_name}.")
    print("Your invoice is displayed below:")
    print(f"Protein: {order[3]} - ${protein_price}")
    print(f"Rice: {order[4]} rice - ${rice_price}")
    print(f"Beans: {order[5]} beans - ${beans_price}")
    print(f"Burrito: {burrito_choice} - ${burrito_price}")
    print(f"Toppings: {topping_list} - ${toppings_price}")
    print(f"Subtotal: ${subtotal}")
    print(f"Discount Code: {discount_code}")
    print(f"Total: ${final_price}")
    print(f"You Save: ${money_saved}")
    print(f"Your order will be ready in {delivery_time} minutes.")
    print("Enjoy your meal and have a good day!")


order_example = ('alex', 'sunderland', 'FLAT3', 'steak', 'brown', 'black', True, 'guacamole', 'sour cream', 'cheese')
process_order(order_example)
