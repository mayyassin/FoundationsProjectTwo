# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Bratz"  

def welcome():
    print("Welcome to %s \nFeel free to shop throughout the stores we have, and only checkout once!" % (site_name))

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    for store in stores:
        print("- %s" % (store))

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store_name.lower() == store.name.lower():
            return store 
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    print("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say goodbyes.")
    
    pick = ""
    while True:
        picked_store = input("")
        if picked_store.lower() == "checkout":
            return "checkout"
        pick = get_store(picked_store)
        if pick == False: 
            print("No store with that name. Please try again. \n")
            picked_store = picked_store.lower()
            pick = get_store(picked_store)
        else:
            return pick


    
    return pick

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above. \nType \"back\" to go back to the main menu where you can checkout. \n")
    choice = ""
    while choice != "back":
        choice = input()
        choice = choice.lower()
        for product in picked_store.products: 
            if choice == product.name.lower(): 
                cart.add_to_cart(product) 
    return choice
            

def shop():
    """
    The main shopping functionality
    """
    #loop until we type checkout
    cart = Cart()
    # your code goes here!
    picked_store = ""
    while picked_store != "checkout":
        picked_store = pick_store()

        if picked_store == "checkout":
            break
        pick_products(cart, picked_store)
    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)