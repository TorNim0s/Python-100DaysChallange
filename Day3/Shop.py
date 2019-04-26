stock = {
    'Steak': 10,
    'Chicken wings': 5,
    'Chicken brest': 25,
    'Water': 20,
    'Sprite': 25,
    'Cola': 15
}

price = {
    'Steak': 21,
    'Chicken wings': 6,
    'Chicken brest': 10,
    'Water': 1,
    'Sprite': 1.5,
    'Cola': 1.5
}

def collect_food():
    food = []
    track = False
    check_stock = False
    print("Enter your shopping list, dont forget for enter each item alone.")
    print("To finish your list enter 0")
    queue = input("enter item")
    while (queue != '0'):
        for items in stock:
            if (queue == items):
                track = True
                if(stock[queue] > 0):
                    food.append(queue)
                    stock[queue] -= 1
                    check_stock = True
        if(track == False):
            print("That item is not on the list")
        elif(check_stock == False):
            print("The stock of the item you chose as been finished")
        check_stock = False;
        track = False;
        queue = input("enter your next item")
    return food


def shopping_cart(foods):
    total_price = 0
    for food in foods:
        total_price+=price[food]
        stock[food]+=1
    return total_price

for food in stock:
    print ("Item Name: " + food + " --- price: " + str(price[food]) + " stock: " + str(stock[food]))
total_stock = collect_food()
total_cost = shopping_cart(total_stock)
print ("Total cost of your list is: " + str(total_cost) + "$")
