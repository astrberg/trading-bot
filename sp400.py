import pandas as pd


symbols = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_400_companies')[0]['Ticker symbol']
symbols.to_csv("s&p400-symbols.csv", header=None)