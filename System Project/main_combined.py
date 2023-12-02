# main_combined.py
from apicall1 import run as apicall_run
from datasave import run as datasave_run
from datashow import run as datashow_run
from final3 import run as final3_run
from finalgui import run as finalgui_run
from emailprint import run as emailprint_run
from gui_mainscreen import run as gui_mainscreen_run
from sendmail import run as sendmail_run
from yearextractor import run as yearextractor_run

def main_combined():
    # Your code here

    print("Running apicall1")
    apicall_run()

    print("Running datasave")
    datasave_run()

    print("Running datashow")
    datashow_run()

    print("Running final3")
    final3_run()

    print("Running finalgui")
    finalgui_run()

    print("Running emailprint")
    emailprint_run()

    print("Running gui_mainscreen")
    gui_mainscreen_run()

    print("Running sendmail")
    sendmail_run()

    print("Running yearextractor")
    yearextractor_run()

    # Your additional code here

if __name__ == "__main__":
    main_combined()
