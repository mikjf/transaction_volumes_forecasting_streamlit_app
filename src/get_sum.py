# IMPORTS
import pandas as pd

###################################################################################

# GET_ARIMA FUNCTION
def get_sum(data, file_name, start_month):
  data = data.set_index('Merchant Name')
  dates = pd.Series(pd.period_range(start_month, freq="M", periods=len(data.columns)))
  data.columns = dates
  data_frame = pd.DataFrame({'Month':dates,'total':data.sum(axis=0).values})
  return data_frame