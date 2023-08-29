# use dialog box with checkmarks for each task
# launch tradovate if checked
# launch tradingview if checked
# launch tos if checked
# launch dashboard if checked

from dotenv import load_dotenv
from tradovate.tradovate import tradovate_script
from tradingview.tradingview import tradingview_script
from tos.tos import tos_script
from dashboard_start.dashboard import dashboard_script
from tkinter import *
from screeninfo import get_monitors


load_dotenv()

def main():
    def run_applications():
        dialog_main.destroy()
        if var_tradovate.get() == 1:
            tradovate_script()
        if var_tradingview.get() == 1:
            tradingview_script()
        if var_tos.get() == 1:
            tos_script()
        if var_dashboard.get() == 1:
            dashboard_script()

    monitor = get_monitors()[0]
    monitor_width = (monitor.width/2)-100
    dialog_main = Tk()
    dialog_main.title("Application Automation")
    dialog_main.geometry(f"200x200+{int(monitor_width)}+200")
    var_tradovate = IntVar(value=1)
    Checkbutton(dialog_main, text="Tradovate", variable=var_tradovate).grid(row=0, column=1, sticky=W)
    var_tradingview = IntVar(value=1)
    Checkbutton(dialog_main, text="Tradingview", variable=var_tradingview).grid(row=1, column=1, sticky=W)
    var_tos = IntVar(value=1)
    Checkbutton(dialog_main, text="TOS", variable=var_tos).grid(row=2, column=1, sticky=W)
    var_dashboard = IntVar(value=1)
    Checkbutton(dialog_main, text="Dashboard", variable=var_dashboard).grid(row=3, column=1, sticky=W)

    Button(dialog_main, text="Run", command=run_applications).grid(row=5, column=1, sticky=W, pady=4)
    Button(dialog_main, text="Quit", command=dialog_main.quit).grid(row=5, column=2, sticky=W, pady=4)

    mainloop()


if __name__ == "__main__":
    main()
