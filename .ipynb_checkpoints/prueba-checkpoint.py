import requests
import json

option=1
def consulta():
    url = f'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_DciePP460ewj5uCIzQWjLqVRtkGXz95ft915eYDS&base_currency={source_currency}&currencies={target_currency}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            converted_amount = data.get('data').get(target_currency)
            if converted_amount:
                print(f'{amount} {source_currency} is equal to {converted_amount*amount} {target_currency}')
            else:
                print('Conversion data not found in the API response.')
                print(data)
        else:
            print(f'Failed to retrieve data. Status code: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
def listado():
    url = f'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_DciePP460ewj5uCIzQWjLqVRtkGXz95ft915eYDS'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            converted_amount = data.get('data')
            if converted_amount:
                print("List:")
                for x in converted_amount:
                    print(x+": "+str(converted_amount[x]))
            else:
                print('Conversion data not found in the API response.')
                print(data)
        else:
            print(f'Failed to retrieve data. Status code: {response.status_code}')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
def solicitudDeDatos():
    option = input("Enter the selected option 1:comvert, 2:list, 3:exit: ").upper()
    source_currency = input("Enter the source currency code: ").upper()
    target_currency = input("Enter the target currency code: ").upper()
    amount = float(input("Enter the amount to convert: "))
#loop para consultar al usuario siempre y cuando no salga de la aplicacion
option='1'
while option!='3':
    option = input("Enter the selected option 1:comvert, 2:list, 3:exit: ")
    if option == '1':
        source_currency = input("Enter the source currency code: ").upper()
        target_currency = input("Enter the target currency code: ").upper()
        amount = float(input("Enter the amount to convert: "))
        consulta()
    elif option == '2':
        listado()
    elif option == '3':
        print("bye")
    else:
        print("this option is not defined")

