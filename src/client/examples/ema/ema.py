import logging

import numpy
from pandas.core.frame import DataFrame
from talib import EMA

import foreverbull
from foreverbull.data.data import Database
from foreverbull.models import OHLC

bull = foreverbull.Foreverbull()

logger = logging.getLogger(__name__)

print("I AM HERE")


def should_hold(df: DataFrame, ema_low, ema_high) -> bool:
    high = EMA(df.price, timeperiod=ema_high)
    if numpy.isnan(high.iloc[-1]):
        return False
    low = EMA(df.price, timeperiod=ema_low)
    if high.iloc[-1] < low.iloc[-1]:
        return True
    return False


@bull.on("stock_data")
def ema(tick: OHLC, database: Database, ema_low=16, ema_high=32):
    pass
    """ # TODO: FIX THIS
    history = database.stock_data(tick.asset.symbol)
    position = database.get_position(tick.asset)
    if should_hold(history, ema_low, ema_high) and position is None:
        return Order(asset=tick.asset, amount=10)
    elif position and should_hold(history, ema_low, ema_high) is False:
        return Order(asset=tick.asset, amount=-10)
    return None
    """
