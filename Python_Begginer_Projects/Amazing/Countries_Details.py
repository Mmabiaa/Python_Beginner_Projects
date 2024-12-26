from countryinfo import CountryInfo
try:
    count = input('Enter the name of the country or -1 to quit: ')
    while count != '-1':
    
        country = CountryInfo(count)

        print("Capital is: ", country.capital())
        print('----------------------------------------------------------------')
        print('Currency is: ', country.currencies())
        print('----------------------------------------------------------------')
        print('Language is: ', country.languages())
        print('----------------------------------------------------------------')
        print('Borders are: ', country.borders())
        print('----------------------------------------------------------------')
        print('Other names are: ', country.alt_spellings())
        print('----------------------------------------------------------------')
        print('Population is: ', country.population())
        print('----------------------------------------------------------------')
        print('Time zone is: ',country.timezones())
        print('----------------------------------------------------------------')
        count = input('Enter the name of the country or -1 to quit: ')
        print('----------------------------------------------------------------')
    else:
        print('Thanks for using the program...')
except KeyError:
    print('Country was not found!')
    print('Try Again with a valid country name.')


# Author - Mmabiaa
