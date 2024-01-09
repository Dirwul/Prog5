from LR5.valutes import Vals


def run():
    valutes = Vals()
    curRates = valutes.getRates()
    for code, info in curRates.items():
        print(f"{info['CharCode']} : {info['Rate']} RUB")
