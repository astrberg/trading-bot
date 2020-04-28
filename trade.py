import alpaca_trade_api as tradeapi
import os
import pandas as pd
from dotenv import load_dotenv
import datetime
load_dotenv()

#For now only trading with fake papers
PAPER_BASE_URL = "https://paper-api.alpaca.markets"

try:
    APCA_API_KEY_ID = os.getenv('APCA_API_KEY_ID')
    APCA_API_SECRET_KEY = os.getenv('APCA_API_SECRET_KEY')
except:
    print("Keys not initialized in the environment please set the \"ALPACA_KEY_ID\" and \"ALPACA_SECRET_KEY\" environment variables")
    exit(-1)

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, PAPER_BASE_URL, api_version='v2') # or use ENV Vars shown below

try:
    symbols = pd.read_csv('./s&p400-symbols.csv', sep=',', names=["ID", "Symbol"])['Symbol'].values
except:
    print("Does the file exists you are looking for?")
    exit(-1)

