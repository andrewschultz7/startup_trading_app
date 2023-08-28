import sqlite3, os, requests, json
from dotenv import load_dotenv

def aqi_to_db():
    load_dotenv()

    aqi_key = os.environ.get("REACT_APP_AQI")
    db_file = "aqi.db"
    url = f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=59901&distance=25&API_KEY={aqi_key}"
    response = requests.get(url)
    aqi_data = json.loads(response.text)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    for data in aqi_data:
                insert_query = """
                    INSERT INTO aqi (DateObserved, HourObserved, AQI)
                    VALUES (?, ?, ?)
                """
                values = (
                    data['DateObserved'],
                    data['HourObserved'],
                    data['AQI']
                )
                cursor.execute(insert_query, values)
    conn.commit()
    conn.close()
