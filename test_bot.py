def test_buy_signal():
    from bot import get_signal
    candles = [
        {"open": 1.1005, "high": 1.1010, "low": 1.1000, "close": 1.1002},
        {"open": 1.1002, "high": 1.1015, "low": 1.1001, "close": 1.1012},
    ]
    assert get_signal(candles) == "BUY / UP"


def test_sell_signal():
    from bot import get_signal
    candles = [
        {"open": 1.1000, "high": 1.1010, "low": 1.0995, "close": 1.1008},
        {"open": 1.1008, "high": 1.1009, "low": 1.0990, "close": 1.0992},
    ]
    assert get_signal(candles) == "SELL / DOWN"


def test_wait_signal():
    from bot import get_signal
    candles = [
        {"open": 1.1000, "high": 1.1010, "low": 1.0995, "close": 1.1005},
        {"open": 1.1005, "high": 1.1008, "low": 1.1000, "close": 1.1003},
    ]
    assert get_signal(candles) == "WAIT"
