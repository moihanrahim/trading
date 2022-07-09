from fyers_api import fyersModel
from fyers_api import accessToken

def place_order(symbol,quantity,side,type):
      client_id ="EGNBLDBRXZ-100"
      access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NTY1MTM5ODcsImV4cCI6MTY1NjU0OTAyNywibmJmIjoxNjU2NTEzOTg3LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaXZHWEQ4REx1T0p1a0Z4NndXWDhlQXcxazE1VzJTWlZ1dE9rNEI1QzhzQnRCVUowc0xMbW1IbEhXZ1E5NTg3cWxEbnhBT2IzZmJRWmdZRmFKQlZBMHVoTlViM3JvNVIzbjlTUVVHbllsbXJMVGpqOD0iLCJkaXNwbGF5X25hbWUiOiJLUklTSE5BS1VNQVIgTU9IQU5SQU0iLCJmeV9pZCI6IlhLMTU5NDAiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.ArWdF76vQRScFr8NwGoCnFdI1cuqFwLqLalCdQK7BNw"
      fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)
      is_async = True

      data = {
            "symbol":symbol,
            "qty":quantity,
            "type": 2 ,
            "side":side,
            "productType":type,
            "limitPrice":0,
            "stopPrice":0,
            "validity":"DAY",
            "disclosedQty":0,
            "offlineOrder":"False",
            "stopLoss":0,
            "takeProfit":0
          }

      print(data)
      print(fyers.place_order(data))




