from dotenv import load_dotenv
from tradovate.tradovate import tradovate_script
from tradingview.tradingview import tradingview_script
from tos.tos import tos_script

load_dotenv()
def main():
    tradovate_script()
    tradingview_script()
    tos_script()

if __name__ == "__main__":
    main()
