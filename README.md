# Weather Data Pipeline with PySpark

This project fetches real-time weather data from the [OpenWeatherMap API](https://openweathermap.org/current), processes it using PySpark, and stores the cleaned output in a CSV file for further analysis or visualization.

---

## Features

- Fetches current weather data for a specified city
- Extracts and transforms essential fields:
  - `timestamp`, `city`, `temperature`, `humidity`, and `description`
- Saves the cleaned dataset to a CSV using Apache Spark
- Easily extensible for scheduled jobs or multi-city batch processing

---

## Technologies Used

- Python 3.10+
- [Apache Spark](https://spark.apache.org/) via `pyspark`
- [findspark](https://github.com/minrk/findspark)
- [OpenWeatherMap API](https://openweathermap.org/api)

---

## Folder Structure

```

.
├── weather.json         # Raw weather data (JSON)
├── weather.csv/         # Output CSV directory from Spark
│   └── part-\*.csv       # Partitioned CSV files
├── Weather.ipynb        # Jupyter notebook for development
├── weather\_pipeline.py  # (Optional) Python script version
└── README.md            # Project documentation

````

---

## ⚙How to Run

1. **Install Dependencies**

```bash
pip install requests findspark pyspark
````

2. **Download and Set Up Spark**
   Follow the [official guide](https://spark.apache.org/downloads.html) to install Spark and configure it properly.

3. **Run the Project**

* Option 1: Run the Jupyter Notebook `Weather.ipynb`
* Option 2: Convert the notebook to a script or use the script version:

```bash
python weather_pipeline.py
```

---

## Sample Output (CSV)

| timestamp           | city    | temperature | humidity | description     |
| ------------------- | ------- | ----------- | -------- | --------------- |
| 2025-06-07 08:10:45 | Nairobi | 17.26       | 83       | overcast clouds |

---

## API Key

This project uses the OpenWeatherMap API. You need to replace the placeholder API key in the script with your actual API key:

```python
API_KEY = "your_api_key_here"
```

Create a free account at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get your API key.

---

## Potential Improvements

* Support for batch processing multiple cities
* Store results in a database (e.g., PostgreSQL or MongoDB)
* Add cron jobs or Airflow for automation
* Visualize data using tools like Power BI or Tableau

---

## Author

**Grace W. Irungu**
📧 [graceirungu96@gmail.com](mailto:graceirungu96@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/grace-w-irungu/)

---

