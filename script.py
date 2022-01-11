def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message
    return get_size()
# create a separate function for print messge & call the function in the else statement. 
# we can place a function below the get size conditionals/control flow and still place a call for it. 
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# added command in line 26 to return order_latte. chatbot can prompt question about milk to the user. can add this command to 'mocha' but would need to add another function and milk options.

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed  Coffee \n[b] Mocha \n[c] Latte \n")
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n [b] Non-fat milk \n[c] Soy milk")
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()
    
def extra_options():
  res = input('Would you like a plastic cup or did you bring your own reusable cup? \n[a] I\'ll need a cup. \n[b] Brought my own! \n> ')
 
  if res == 'a':
    print('Okay, no problem! We\'ll get you a plastic cup.')
  elif res == 'b':
    print('Great! We\'ll fill up your reusable cup.')
  else:
    print_message()
    return extra_options()

def coffee_bot():
  print('Welcome to the cafe!')

coffee_bot()

size = get_size()
print(size)

drink_type = get_drink_type()
print(drink_type)

print("Alright, that's a " + size  + drink_type )

name = input("Can I get your name please? ")

print("Thanks, " +  name  + "Your drink will be ready shortly.")
