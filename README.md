
# Pokémon ETL Project

This repository demonstrates an automated ETL (Extract, Transform, Load) pipeline for Pokémon data, featuring real-time monitoring of changes to the source file using the `watchdog` library.

---

## Project Overview

This project aims to:
- **Extract** Pokémon data from a CSV file.
- **Transform** the data to fix inconsistencies and enhance usability.
- **Load** the cleaned data into an SQLite database.
- **Monitor** changes to the source file and rerun the ETL pipeline automatically when updates are detected.

The project uses Python scripts and a sample dataset to showcase a complete ETL pipeline.

---

## Repository Contents

1. **`Pokemon.csv`**:  
   A dataset containing Pokémon information with columns such as:
   - `number`, `name`, `type1`, `type2`, `total`, `hp`, `attack`, `defense`, `sp_attack`, `sp_defense`, `speed`, `generation`, `legendary`.

   This file is monitored for changes, and any updates trigger the ETL process.

2. **`pokemon_etl_monitor.py`**:  
   A Python script that automates and monitors the ETL process:
   - **Extraction**: Reads the Pokémon data from the CSV file.
   - **Transformation**:
     - Fills missing `type2` values with the corresponding `type1`.
     - Corrects Pokémon entries with `generation` set to `0` by updating them to `7`.
     - Splits the data into two categories: `original_forms` (unique Pokémon) and `other_forms` (alternative forms like Mega or Gigantamax).
   - **Loading**: Stores the cleaned and transformed data in an SQLite database with two tables:
     - `original_forms`: Unique Pokémon entries.
     - `other_forms`: Alternative forms.
   - **Monitoring**: Uses the `watchdog` library to detect changes in the source CSV file and automatically rerun the ETL process.

3. **`pokemon ETL.ipynb`**:  
   A Jupyter Notebook providing a step-by-step implementation of the ETL pipeline for analysis and experimentation.

---

## Prerequisites

### Required Libraries
Install the following Python libraries to run the project:
```bash
pip install pandas numpy watchdog
```

### Database
SQLite is used for storing processed data. Ensure your system supports SQLite (included by default in Python).

---

## Usage

### 1. Running the Monitoring Script
1. Place the `Pokemon.csv` file in the same directory as `pokemon_etl_monitor.py`.
2. Run the script:
   ```bash
   python pokemon_etl_monitor.py
   ```
3. The script will:
   - Monitor `Pokemon.csv` for changes.
   - Automatically execute the ETL process whenever the file is updated.
   - Store the cleaned data in `pokemon.db` with two tables: `original_forms` and `other_forms`.

### 2. Exploring the SQLite Database
After the ETL process, explore the data stored in `pokemon.db` using SQLite tools:
```bash
sqlite3 pokemon.db
```
Run SQL queries to analyze the cleaned Pokémon data.

### 3. Using the Jupyter Notebook
Open `pokemon ETL.ipynb` to:
- Test and debug the ETL pipeline.
- Analyze and visualize the data.

---

## Key Features

- **Real-Time Monitoring**: Automatically detects updates to the Pokémon dataset and reruns the ETL pipeline.
- **Data Cleaning**:
  - Fills missing values in the secondary Pokémon type (`type2`).
  - Corrects invalid generation values.
- **Data Organization**: Splits the data into unique and alternative forms for easier analysis.
- **SQLite Integration**: Stores the processed data in a database for further use.

---

## Contribution

Contributions are welcome! Suggestions for new features, performance improvements, or bug fixes are highly appreciated.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
