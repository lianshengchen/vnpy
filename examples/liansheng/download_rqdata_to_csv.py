import rqdatac as rq
from rqdatac import *
import pandas as pd

rq.init()


rq_result = rq.get_price('000001.XSHE','2019-1-1','2019-2-01','tick')
df = pd.DataFrame(rq_result)
df.to_csv('000001.XSHE.csv')

