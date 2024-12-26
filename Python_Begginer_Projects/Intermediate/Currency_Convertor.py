# Currency conversion rates relative to USD
currency_rates = {
    'USD': 1.0,      # Base currency
    'EUR': 0.85,     # Euro
    'GBP': 0.75,     # British Pound
    'JPY': 110.0,    # Japanese Yen
    'AUD': 1.35,     # Australian Dollar
    'CAD': 1.25,     # Canadian Dollar
    'CHF': 0.92,     # Swiss Franc
    'CNY': 6.45,     # Chinese Yuan
    'INR': 73.0,     # Indian Rupee
    'BRL': 5.2,      # Brazilian Real
    'GHC': 15.71     # Ghana Cedis
}

def convert_currency(amount, from_currency, to_currency, rates):
    if (from_currency not in rates) or to_currency not in rates:
        raise ValueError('Invalid currency')
    
    #Convert amount to USd first
    amount_in_usd = amount / rates[from_currency]

    #Convert from usd to target currency
    converted_amount = amount_in_usd * rates[to_currency]

    return converted_amount

def main():
    while True:
        print('Welcome to the Currency Converter! 👌')
        print('Available currencies: ', ','.join(currency_rates.keys()))

        try:
            amount = float(input('Enter the amount to convert: '))
            from_currency = input('Enter the currency code you are converting from: ')
            to_currency = input('Enter the currency code you are converting to: ')

            converted_amount = convert_currency(amount, from_currency, to_currency, currency_rates)
            print(f'{amount} {from_currency} == {converted_amount:.2f} {to_currency}')
        except:
            print('Invalid Input')
        
        options = ('y', 'n')
        Continue = input('Do more conversions (y/n): ').lower()
        if Continue not in options:
            print('Invalid options')
        
        else:
            if Continue == 'n':
                print('Thanks for using the programming...😁')
                break
            else:
                print('')


main()
# Author - Mmabiaa
