from enum import Enum

class CurrencyType(str,Enum):
    EUR = "EUR"
    USD = "USD"
    RON = "RON"
    MDL = "MDL"
    UAH = "UAH"