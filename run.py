import pysd
import pandas as pd
import numpy as np

# model = pysd.read_xmile('xmile/teacup.xmile', missing_values="warning")
model = pysd.load('models/vidzeme-combined.py', missing_values="warning")

print(model.doc())
# temp = pd.Series(index=np.array([2020,2040]), data=np.array([1,5]))
def t(x=None):
    series = pd.Series(index=np.array([2020,2040]), data=np.array([1,5]))
    retval = np.interp( x if x != None else model.time(), series.index, series.values)
    # print("%s -> %s" % (model.time(), retval))
    return retval

# params={"farm_to_fork_effect_on_industry": temp}

model.set_components({"farm_to_fork_effect_on_industry": t})

# stocks = model.run(params=params)
stocks = model.run()
stocks = model.run()


# print (stocks)
# print (stocks["related_agricultural_jobs_on_industry"])

# for n in stocks.columns:
#     print(n)
# print(stocks.columns)