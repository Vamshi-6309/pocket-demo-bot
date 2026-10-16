def get_signal(candles):
    if len(candles) < 2:
        return "WAIT"

    first = candles[-2]
    second = candles[-1]

    # BUY:
    # First candle RED
    # Second candle GREEN
    # Green candle closes above red candle high
    if (
        first["close"] < first["open"]
        and second["close"] > second["open"]
        and second["close"] > first["high"]
    ):
        return "BUY / UP"

    # SELL:
    # First candle GREEN
    # Second candle RED
    # Red candle closes below green candle low
    if (
        first["close"] > first["open"]
        and second["close"] < second["open"]
        and second["close"] < first["low"]
    ):
        return "SELL / DOWN"

    return "WAIT"
