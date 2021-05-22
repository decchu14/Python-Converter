from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input("Enter the Amount: "))

from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
result = c.convert(from_currency, to_currency, amount)
print(result)
