from common import MyLogger
from datetime import datetime
from vnpy.trader.utility import extract_vt_symbol
from vnpy.trader.object import HistoryRequest
from vnpy.trader.constant import Interval, Exchange
from vnpy.trader.rqdata import rqdata_client
from vnpy.trader.database import database_manager
import traceback
import rqdatac as rq 
from rqdatac import get_price
from vnpy.trader.object import BarData
from typing import List

"""vpn.trade.rqdata.py"""
def run_downloading(
        rq_symbol: str,
        exchange: str,
        interval: str,
        start: datetime,
        end: datetime
    ):
        """
        vpn.trade.rqdata.query_history()
        """
        myLogger = MyLogger()
        myLogger.info(f"{rq_symbol}-{interval} starting download")

        try:
            df = get_price(
                rq_symbol,
                frequency=interval,
                fields=["open", "high", "low", "close", "volume", "open_interest"],
                start_date=start,
                end_date=end,
                adjust_type="none"
                )
            myLogger.info(f"finished download row={df.shape[0]};fieds={df.shape[1]}")

            data: List[BarData] = []
            if df is not None:
                for ix, row in df.iterrows():
                    #myLogger.info(f"rq_symbol={rq_symbol};exchange={exchange}")
                    bar = BarData(
                        symbol=rq_symbol,
                        exchange=exchange,
                        interval=Interval(interval),
                        datetime=row.name.to_pydatetime() ,
                        open_price=row["open"],
                        high_price=row["high"],
                        low_price=row["low"],
                        close_price=row["close"],
                        volume=row["volume"],
                        open_interest=row["open_interest"],
                        gateway_name="RQ"
                    )
                    data.append(bar)
                    
                    
            if data:
                database_manager.save_bar_data(data)
                myLogger.info(f"{rq_symbol}-{interval} download finished")
            else:
                myLogger.info(f"download failed, cannot get {rq_symbol} history data")
        except Exception:
            msg = f"download exception :\n{traceback.format_exc()}"
            myLogger.info(msg)


myLogger = MyLogger()
rq.init()
myLogger.info("download 01")
run_downloading("TA2001",Exchange.CZCE,"1m","2019-01-04","2020-02-15")
myLogger.info("download 02")
run_downloading("TA2002",Exchange.CZCE,"1m","2019-01-04","2020-02-15")
myLogger.info("download 03")
run_downloading("TA2003",Exchange.CZCE,"1m","2019-01-04","2020-02-15")
myLogger.info("download 04")
run_downloading("TA2004",Exchange.CZCE,"1m","2020-01-01","2020-02-15")
myLogger.info("download 05")
run_downloading("TA2005",Exchange.CZCE,"1m","2020-01-01","2020-02-15")
myLogger.info("download 06")
run_downloading("TA2006",Exchange.CZCE,"1m","2020-01-01","2020-02-15")
myLogger.info("download 07")
run_downloading("TA2007",Exchange.CZCE,"1m","2020-01-01","2020-02-15")
myLogger.info("download 08")
run_downloading("TA2008",Exchange.CZCE,"1m","2020-01-01","2020-02-15")
myLogger.info("download 09")
run_downloading("TA2009",Exchange.CZCE,"1m","2020-01-01","2020-02-15")
myLogger.info("download 10")
run_downloading("TA2010",Exchange.CZCE,"1m","2020-01-01","2020-02-15")
myLogger.info("download 11")
run_downloading("TA2011",Exchange.CZCE,"1m","2020-01-01","2020-02-15")
myLogger.info("download 12")
run_downloading("TA2012",Exchange.CZCE,"1m","2020-01-01","2020-02-15")
myLogger.info("download finished")



