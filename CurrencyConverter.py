# Offline Currency Converter with fixed exchange rates
# Example exchange rates (as of a specific date; rates may not be up to date)
exchange_rates = {
    'USD': {
        'INR': 83.35,
        'EUR': 0.92,
        'GBP': 0.78
    },
    'INR': {
        'USD': 0.012,
        'EUR': 0.011,
        'GBP': 0.0094
    },
    'EUR': {
        'USD': 1.09,
        'INR': 90.7,
        'GBP': 0.85
    },
    'GBP': {
        'USD': 1.28,
        'INR': 96.5,
        'EUR': 1.18
    }
}
def convert_currency(amount, base_currency, target_currency):
    try:
        rate = exchange_rates[base_currency][target_currency]
        converted_amount = amount * rate
        return converted_amount, rate
    except KeyError:
        raise ValueError("Exchange rate not available for the selected currency pair.")
def main():
    print("Offline Currency Converter")
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., INR): ").upper()
    try:
        amount = float(input(f"Enter amount in {base_currency}: "))
        converted, rate = convert_currency(amount, base_currency, target_currency)
        print(f"\nExchange Rate: 1 {base_currency} = {rate:.4f} {target_currency}")
        print(f"{amount:.2f} {base_currency} = {converted:.2f} {target_currency}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()