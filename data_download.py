import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    print()

def calculate_and_display_average_price(data):
    return data['Close'].mean()
    
def export_data_to_csv(data, filename):
    try:
        data.to_csv(filename, index=False)
    except Exception as e:
        print(f'Не удалось экспортировать данные в CSV. Ошибка: {e}')
