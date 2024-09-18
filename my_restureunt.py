def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0
    while True:
        try:
            total = inpuo(menu, total)
        except EOFError:
            print()
            break

def inpuo(menu, total):
    order = input("Do you like to order anything? ").title()
    if order in menu:
        total += menu[order]
        print(f"Total: ${total:.2f}")
    else:
        print("Item not found.")
    return total
if __name__ == "__main__":

 main()
