import json


class RatesParser:
    def __init__(self, filepath):
        rates_data = self._open_json_file(filepath)
        self.base_rate = rates_data["base"]  # metadata
        self.date = rates_data["date"]
        self.gbp = rates_data["rates"]["GBP"]
        self.usd = rates_data["rates"]["USD"]
        self.jpy = rates_data["rates"]["JPY"]

    def _open_json_file(self, filepath: str) -> dict:
        with open(filepath) as jsonfile:
            return json.load(jsonfile)


if __name__ == "__main__":
    rp = RatesParser("exchange_rates.json")
    print(rp.base_rate)
    print(rp.date)
    print(rp.gbp)
    print(rp.usd)
    print(rp.jpy)
