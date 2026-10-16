import os
import time
import requests


def get_signal(candles):
    if len(candles) < 2:
        return "WAIT"

    first = candles[-2]
    second = candles[-1]

    if (
        first["close"] < first["open"]
        and second["close"] > second["open"]
        and second["close"] > first["high"]
    ):
        return "BUY / UP"

    if (
        first["close"] > first["open"]
        and second["close"] < second["open"]
        and second["close"] < first["low"]
    ):
        return "SELL / DOWN"

    return "WAIT"


def get_candles():
    api_key = os.environ.get("TWELVE_DATA_API_KEY")
    if not api_key:
        raise RuntimeError("API key secret is not configured.")

    response = requests.get(
        "https://api.twelvedata.com/time_series",
        params={
            "symbol": "EUR/USD",
            "interval": "1min",
            "outputsize": 10,
            "apikey": api_key,
            "timezone": "UTC",
        },
        timeout=20,
    )
    response.raise_for_status()
    data = response.json()

    if "values" not in data:
        raise RuntimeError("Candle data unavailable from provider.")

    candles = []
    for item in reversed(data["values"]):
        candles.append({
            "open": float(item["open"]),
            "high": float(item["high"]),
            "low": float(item["low"]),
            "close": float(item["close"]),
            "time": item["datetime"],
        })

    return candles


if __name__ == "__main__":
    print("EUR/USD demo signal bot started.")
    try:
        candles = get_candles()
        # Exclude the newest candle because it may still be forming.
        closed_candles = candles[:-1]
        print("Latest closed candle:", closed_candles[-1]["time"])
        print("DEMO SIGNAL:", get_signal(closed_candles))
        print("Demo signal only; no trades placed.")
    except Exception as error:
        print("Signal unavailable:", error)
