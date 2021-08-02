from forex_python.converter import CurrencyRates
import decimal

c = CurrencyRates()

rate = c.convert('USD', 'INR', 1)  # convert('USD', 'INR', 10)

rate= decimal.Decimal(rate)
