# API fetch from AQI to database
# start React

import subprocess, os
from dashboard_start.aqi_import import aqi_to_db

def dashboard_script():
    def start_react():
        aqi_to_db()
        start_path = (os.path.dirname(os.path.abspath(__file__)))
        try:
            subprocess.run(["npm", "start"], cwd=start_path, shell=True)
        except FileNotFoundError:
            print("react trouble starting")

    start_react()
