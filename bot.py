def get_signal(candles):
    if len(candles) < 2:
        return "WAIT"

    red = candles[-2]
    green = candles[-1]

    if (
        red["close"] < red["open"]
        and green["close"] > green["open"]
        and green["close"] > red["high"]
    ):
        return "BUY / UP"

    return "WAIT"


if __name__ == "__main__":
    candles = [
        {"open": 1.1050, "high": 1.1060, "close": 1.1040},
        {"open": 1.1040, "high": 1.1070, "close": 1.1065},
    ]

    print(get_signal(candles))
