# ##########################
# Imports
# ##########################
import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib as plt
from matplotlib import style


# ##########################
# CODE
# ##########################
style.use('fivethirtyeight')

start = datetime.datetime(2016, 7, 1)
end = datetime.datetime(2016, 7, 31)
empresa = "PBR"
ptbr = web.get_data_yahoo(empresa, start, end)
ptbr.head(20)



