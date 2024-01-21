import requests
import logging


class CurrencyConverter:
    BASE_URL = "https://currency-exchange.p.rapidapi.com/exchange"

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com",
        }

    def _make_request(self, params):
        response = requests.get(self.BASE_URL, headers=self.headers, params=params)
        return (
            response.status_code,
            response.json() if response.status_code == 200 else None,
        )

    def get_exchange_rate(self, from_currency, to_currency, amount=1.0):
        params = {"from": from_currency, "to": to_currency, "q": amount}
        status_code, data = self._make_request(params)

        if data:
            return data
        else:
            logging.warning(f"Failed to retrieve exchange rate. Error: {status_code}")
            return None

    def fetch_and_log_exchange_rate(self, from_currency, to_currency, amount=1.0):
        exchange_rate = self.get_exchange_rate(from_currency, to_currency, amount)

        if exchange_rate:
            logging.info(
                f"Exchange rate from {from_currency} to {to_currency} for {amount} is: {exchange_rate}"
            )
        else:
            logging.warning("Failed to retrieve exchange rate.")