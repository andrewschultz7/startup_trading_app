import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [weatherData, setWeatherData] = useState([]);
  const [aqiData, setAqiData] = useState([]);

  useEffect(() => {
    const apiKey = process.env.REACT_APP_WEATHER;
    fetch(`http://api.weatherapi.com/v1/forecast.json?key=${apiKey}&q=auto:ip&days=7`)
      .then(response => response.json())
      .then(apiData => setWeatherData(apiData))
      .catch(error => console.error("Error fetching data: ", error));
  }, []);

  useEffect(() => {
    const apiKey = process.env.REACT_APP_AQI;
    const url = `https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=59901&distance=25&API_KEY=${apiKey}`;
    async function fetchData() {
      try {
        const response = await fetch(url);
        const apiData = await response.json();
        setAqiData(apiData);
      } catch (error) {
        console.error("Error fetching AQI data: ", error);
      }
    }
    fetchData();
  }, []);

  const maxAQI = aqiData.reduce((max, sensor) => Math.max(max, sensor.AQI), 0)

  return (
    <div className="App">
        {weatherData.current && (<p>Feels like: {weatherData.current.feelslike_f}</p>)}

        {aqiData && (<p>AQI: {maxAQI}</p>)}
    </div>
  );
}

export default App;
