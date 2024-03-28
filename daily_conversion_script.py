import json
import urllib.request

URL = 'https://www.floatrates.com/daily/usd.json'

def open_url(URL): # Open URL link, load JSON data, return as buffer
    with urllib.request.urlopen(URL) as url:
        data = json.load(url)
        #print(data)
    return data

def write2json(data): # Write buffer into json file
    with open('daily_rates.json', 'w') as f:
        json.dump(data, f, indent=2)

def openJson(): # Open and return json file as dictionary
    with open('daily_rates.json', 'r+') as f:
        var = json.load(f)
        #print(f"Inside openJson and object is of type: {type(var)}")

    ''' # Print key and values
    for key in var: #iterate through json file
        value = var[key]
        print(f"The key and value are ({key}) = ({value})")
        print(f"{xar[key]['code']}: {xar[key]['name']: <40} Rate: {xar[key]['rate']}") #Print specific values
    '''
    return var

def prep_work(): # Initiate and return working buffer
    write2json(open_url(URL)) # Open URL and write data to JSON file
    buffer = openJson() # Load JSON file into buffer dictionary we'll work with
    #print(f"Inside prep_work() function. The working object is of TYPE: {type(buffer)}")
    #print(buffer)
    return buffer

def print_all_key_values(var): # Print key and values in working buffer
    #print("Inside the print_all function.")
    #print(len(var))
    #print(var['mxn']) # Print specific json object by code, i.e. Mexico
    for key in var:
        #print("inside for loop")
        value = var[key]
        #rate = float(xar[key]['rate'])
        print(f"The key and value are ({key}) = ({value})")
        #print(f"{xar[key]['code']}: {xar[key]['name']: <40} Rate: {xar[key]['rate']: <20} Inverse Rate: {xar[key]['inverseRate']}")

# Print user conversion rate by user choice
# Called by ask_user() function
def print_user_rate_choice(CODE, buffer, AMOUNT, option):
        #xar = openJson()
        CODE = CODE.lower()
        #print(CODE)
        #print(f"Code/Country: {buffer[CODE]['code']}/{buffer[CODE]['name']} \
        #\nRate: {buffer[CODE]['rate']} Inverse Rate: {buffer[CODE]['inverseRate']}")

        inverse_rate = float(buffer[CODE]['inverseRate'])
        rate = float(buffer[CODE]['rate'])
        symbol = (buffer[CODE]['code']).upper()
        country = str(buffer[CODE]['name'])
        date_requested = str(buffer[CODE]['date'])

        # Print statements based on RATE or INVERSE RATE
        if option == '1':
            print(f"The currency exchange between USD/{symbol} is {round(float(rate), 2)}")
            print(f"The USD ${AMOUNT} would be {buffer[CODE]['name']} ${round(float(AMOUNT * rate), 2)}.")
        if option == '2':
            print(f"The inverse exchange between USD/{symbol} is {round(float(inverse_rate), 2)}")
            print(f"The {CODE.upper()} ${AMOUNT} would be USD ${round(float(AMOUNT * inverse_rate), 2)}.")



# Print Country Code and Country Name
def print_country_codes(buffer):
    #dict(sorted(buffer.items()))
    #buffer = sort_currencies(buffer)
    print("Code: Country")
    for key in buffer:
        value = buffer[key]
        print(f"{buffer[key]['code']}: {buffer[key]['name']: <40}")

# Print USD/Country Rates & Inverse Rates
def print_rates_and_inverse(buffer, var):

    print("Code: Country")
    for key in buffer:
        value = buffer[key]
        if var == 'all':
            print(f"{buffer[key]['code']}: {buffer[key]['name']: <40} \nRATE: {buffer[key]['rate']} INVERSE RATE: {buffer[key]['inverseRate']}")
        if var == 'rate':
            print(f"{buffer[key]['code']}: {buffer[key]['name']: <40} RATE: {buffer[key]['rate']}")
        if var == 'inverse':
            print(f"{buffer[key]['code']}: {buffer[key]['name']: <40} INVERSERATE: {buffer[key]['inverseRate']}")

# Ask user for input to convert currency
def ask_user(buffer):
    requested_amount = ''
    requested_code = input("Please enter a country code: ")
    try:
        for char in requested_code:
            if char.isalpha():
                print(char)
        if isinstance(requested_code, str):
            requested_code = requested_code.upper()
            print(f'Type of variable {requested_code} is {type(requested_code)}.')
            check_if_key_exists(buffer, requested_code)
    except:
        print("Error.")

    # Options for converting currencies
    print(f"1 - USD to {requested_code.upper()}\t2 - {requested_code.upper()} to USD")
    var = input(f"Convert from USD to {requested_code.upper()} or {requested_code.upper()} to USD? ")

    if var == '1': # Convert from USD to New Currency
        requested_amount = float(input("Please enter dollar amount you wish to convert: $"))
        #print_single_rate(requested_code, buffer, requested_amount)
        print_user_rate_choice(requested_code, buffer, requested_amount, var)
    if var == '2': # Convert from New Currency to USD
        requested_amount = float(input("Please enter currency amount you wish to convert: $"))
        #print_inverse_rate(requested_code, buffer, requested_amount)
        print_user_rate_choice(requested_code, buffer, requested_amount, var)

# Ask user for country code to print its specific values
def get_single_key(buffer):
    key = input("Please enter a country code to see its rates: ")
    key = key.lower()
    print("CODE RATE \tINVERSE RATE")
    print(buffer[key]['code'], buffer[key]['rate'], buffer[key]['inverseRate'])

# Check if Country Code exists
def check_if_key_exists(buffer, choice):
    for key in buffer:
        value = buffer[key]
        #print(buffer[key]['code'])
        if choice == buffer[key]['code']:
            #print(buffer[key]['code'])
            #print(f"Match found for choice <{choice}> with matching code <{buffer[key]['code']}>.")
            break
        else:
            pass
            #print('No match found')
    print(f"Match found for choice <{choice}> with matching code <{buffer[key]['code']}>.")


# Generic sort by function, passes value you want sorted by
def sort_by(buffer, VALUE):
    sorted_dict = dict(sorted(buffer.items(), key=lambda item: item[1][VALUE], reverse=True))
    print(f"This sorted currencies object is of TYPE: {type(sorted_dict)}")
    return sorted_dict

# Print date the JSON URL data was pulled
def date_data_pulled(buffer):
    for key in buffer:
        value = buffer[key]
        date = buffer[key]['date']
    print(f"Date pulled: {date}")

# Main Menu with choices
def main_menu(buffer):
    option = ''
    count = 0
    print("Entering Main Menu.")

    choice0 = 'Print all key and values'
    choice1 = 'Print Country Codes'
    choice2 = 'Print Rates & Inverse Rates'
    choice3 = 'Print currency rates sorted from high to low'
    choice4 = 'Print currency inverse rates sorted from high to low'
    choice5 = 'Print date data pulled from URL'
    choice6 = 'Print rates and inverse rates for specific Country Code'
    choice10 = 'Convert USD Amount to Country Code Currency'

    while option != '00':
        if count > 0:
            print('\n' + ("=" * 80))
        print(f"Options are\n00 - Exit program \n0 - {choice0} \
            \n1 - {choice1} \n2 - {choice2} \n3 - {choice3} \
            \n4 - {choice4} \n5 = {choice5} \n6 - {choice6}\
            \n10 - {choice10}\n")

        option = input("Please select an option: ")
        if option == '0': # Print all keys and values
            print_all_key_values(buffer)
        elif option == '1': # Print Country Codes
            var = sort_by(buffer, 'name')
            print_country_codes(var)
        elif option == '2': # Print Rates & Inverse Rates
            #var = sort_by(buffer, 'inverseRate')
            print_rates_and_inverse(buffer, 'all')
        elif option == '3': # Print currency rates sorted from high to low
            print("Country Currency sorted by rate from low to high:")
            var = sort_by(buffer, 'rate')
            print_rates_and_inverse(var, 'rate')
        elif option == '4': # Print currence inverse rates sorted from high to low
            print("Country Currency sorted by inverse rate from low to high:")
            var = sort_by(buffer, 'inverseRate')
            print_rates_and_inverse(var, 'inverse')
        elif option == '5': # Print date data pulled
            date_data_pulled(buffer)
        elif option == '6':
            print("Insert new function call here.")
            get_single_key(buffer)
        elif option == '10': # Convert Currencies
            ask_user(buffer)

        count += 1

    print("Now exiting Main Menu. Goodbye!")


def main():
    buffer = prep_work()
    main_menu(buffer)

if __name__ == '__main__':
    main()
