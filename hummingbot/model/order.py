#!/usr/bin/env python

from sqlalchemy import (
    Column,
    Text,
    Index,
    BigInteger,
    Float
)
from sqlalchemy.orm import relationship

from . import HummingbotBase


class Order(HummingbotBase):
    __tablename__ = "Order"
    __table_args__ = (Index("o_config_timestamp_index",
                            "config_file_path", "creation_timestamp"),
                      Index("o_market_symbol_timestamp_index",
                            "market", "symbol", "creation_timestamp"),
                      Index("o_market_base_asset_timestamp_index",
                            "market", "base_asset", "creation_timestamp"),
                      Index("o_market_quote_asset_timestamp_index",
                            "market", "quote_asset", "creation_timestamp"))

    id = Column(Text, primary_key=True, nullable=False)
    config_file_path = Column(Text, nullable=False)
    strategy = Column(Text, nullable=False)
    market = Column(Text, nullable=False)
    symbol = Column(Text, nullable=False)
    base_asset = Column(Text, nullable=False)
    quote_asset = Column(Text, nullable=False)
    creation_timestamp = Column(BigInteger, nullable=False)
    order_type = Column(Text, nullable=False)
    amount = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    last_status = Column(Text, nullable=False)
    last_update_timestamp = Column(BigInteger, nullable=False)
    status = relationship("OrderStatus", back_populates="order")
    trade_fills = relationship("TradeFill", back_populates="order")

    def __repr__(self) -> str:
        return f"Order(id={self.id}, config_file_path='{self.config_file_path}', strategy='{self.strategy}', " \
            f"market='{self.market}', symbol='{self.symbol}', base_asset='{self.base_asset}', " \
            f"quote_asset='{self.quote_asset}', creation_timestamp={self.creation_timestamp}, " \
            f"order_type='{self.order_type}', amount={self.amount}, price={self.price}, " \
            f"last_status='{self.last_status}', last_update_timestamp={self.last_update_timestamp})"
