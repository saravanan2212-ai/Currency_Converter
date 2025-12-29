import requests

API_KEY = "9b12f669ad9d74771a37c254"  # Replace with your API key
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def fetch_exchange_rates(base_currency):
    """Fetches exchange rates for the given base currency."""
    try:
        response = requests.get(BASE_URL + base_currency)
        data = response.json()
        
        if data['result'] != 'success':
            print("❌ Error fetching exchange rates. Please check your API key or currency code.")
            return None
        
        return data['conversion_rates']
    
    except requests.exceptions.RequestException as e:
        print("❌ Network error:", e)
        return None

def convert_currency(rates, target_currency, amount):
    """Converts amount to target currency using fetched rates."""
    try:
        rate = rates[target_currency]
        return amount * rate
    except KeyError:
        print(f"❌ Error: {target_currency} is not a supported currency.")
        return None

def main():
    print("💱 Welcome to the Perfect Currency Converter 💱")
    
    while True:
        base_currency = input("Enter base currency (e.g., USD): ").upper()
        rates = fetch_exchange_rates(base_currency)
        if rates is None:
            continue
        
        print("Available currencies:", ", ".join(rates.keys()))
        target_currency = input("Enter target currency: ").upper()
        
        amount_input = input(f"Enter amount in {base_currency}: ")
        if not amount_input.replace(".", "", 1).isdigit():
            print("❌ Invalid amount! Please enter a number.")
            continue
        
        amount = float(amount_input)
        converted_amount = convert_currency(rates, target_currency, amount)
        
        if converted_amount is not None:
            print(f"✅ {amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        
        again = input("Do you want to convert another amount? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the Currency Converter! 💰")
            break

if __name__ == "__main__":
    main()
