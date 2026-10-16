def get_signal(candles):
    if len(candles) < 2:
        return "WAIT"

    first = candles[-2]
    second = candles[-1]

    # BUY: red candle followed by green breakout
    if (
        first["close"] < first["open"]
        and second["close"] > second["open"]
        and second["close"] > first["high"]
    ):
        return "BUY / UP"

    # SELL: green candle followed by red breakdown
    if (
        first["close"] > first["open"]
        and second["close"] < second["open"]
        and second["close"] < first["low"]
    ):
        return "SELL / DOWN"

    return "WAIT"


if __name__ == "__main__":
    print("EUR/USD demo signal bot ready.")
    print("This file contains signal logic only.")
    print("No trades will be placed.")
