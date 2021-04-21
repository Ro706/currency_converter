#python 3.7.1
currency = 'USD'
while currency != exit:
    amount = float(input("Enter amount to convert in rupees:\n"))
    print("Available Currencies: USD, EUR, GBP, JPY, AUD (u,e,g,j,a)")
    currency = input("Enter Currency Code:\n")

    u = 'USD'
    e = 'EUR'
    g = 'GBP'
    j = 'JPY'
    a = 'AUD'

    def convert():
        if currency == 'u':
            new_amount = amount * (1.0/74.74)
            print(f"Your amount in {u} is {new_amount}")
  
        elif currency == 'e':
            new_amount = amount * (1.0/90.2)
            print(f"Your amount in {e} is {new_amount}")
    
        elif currency == 'g':
            new_amount = amount * (1.0/104.54)
            print(f"Your amount in {g} is {new_amount}")
  
        elif currency == 'j':
            new_amount = amount * (1.0/0.69)
            print(f"Your amount in {j} is {new_amount}")
  
        elif currency == 'a':
            new_amount = amount * (1.0/59.27)
            print(f"Your amount in {a} is {new_amount}")
            
        elif currency == 'exit':
            exit()
        else:
            print('error')      

    convert()
