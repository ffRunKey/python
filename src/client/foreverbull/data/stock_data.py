from sqlalchemy import Column, Date, Float, Integer, Numeric, String
from sqlalchemy.orm import declarative_base, relation
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class Instrument(Base):
    __tablename__ = "instrument"
    isin = Column("isin", String, primary_key=True)
    wkn = Column("wkn", String)
    symbol = Column("symbol", String)
    name = Column("name", String)
    title = Column("title", String)
    instrument_type = Column("instrument_type", String)


class OHLC(Base):
    __tablename__ = "ohlc"
    id = Column("id", Integer, primary_key=True)
    isin = Column("isin", Integer, ForeignKey("instrument.isin"))
    instrument = relation("Instrument")
    open = Column("open", Numeric)
    high = Column("high", Numeric)
    low = Column("low", Numeric)
    close = Column("close", Numeric)
    volume = Column("volume", Integer)
    time = Column("time", Date)


class Position(Base):
    __tablename__ = "position"
    id = Column("id", Integer, primary_key=True)
    isin = Column("isin", Integer, ForeignKey("instrument.isin"))
    instrument = relation("Instrument")
    portfolio_id = Column("portfolio_id", Integer, ForeignKey("portfolio.id"))
    portfolio = relation("Portfolio", back_populates="positions")
    amount = Column("amount", Integer)
    cost_basis = Column("cost_basis", Float)
    last_sale_price = Column("last_sale_price", Float)
    last_sale_date = Column("last_sale_date", Date)


class Portfolio(Base):
    __tablename__ = "portfolio"
    id = Column("id", Integer, primary_key=True)
    execution_id = Column("execution", String)
    cash_flow = Column("cash_flow", Float)
    starting_cash = Column("starting_cash", Integer)
    portfolio_value = Column("portfolio_value", Float)
    pnl = Column("pnl", Float)
    returns = Column("_returns", Float)
    start_date = Column("start_date", Date)
    current_date = Column("_current_date", Date)
    positions_value = Column("positions_value", Float)
    positions_exposure = Column("positions_exposure", Float)
    positions = relation("Position", back_populates="portfolio")
