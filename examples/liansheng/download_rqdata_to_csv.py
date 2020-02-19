import rqdatac as rq
from rqdatac import *
import pandas as pd

rq.init()


#rq_result = rq.get_price('000001.XSHE','2018-1-1','2018-12-31','tick')
rq_result = get_price('000001.XSHE',start_date='2019-1-1',end_date='2019-12-31',frequency=interval,
                fields=["open", "high", "low", "close", "volume", "open_interest"],
                adjust_type="none"
                )
df = pd.DataFrame(rq_result)
df.to_csv('000001.XSHE.2019.bar1m.csv')

