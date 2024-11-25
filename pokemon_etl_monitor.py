import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
import sqlite3


# Define ETL tasks
def extract(file_path):
    """Extract Pokémon data from CSV."""
    print("Extracting data...")
    return pd.read_csv(file_path)


def transform(pokemon):
    """Transform Pokémon data."""
    print("Transforming data...")
    # Fill missing values in Type 2 with Type 1
    pokemon['type2'] = pokemon['type2'].fillna(pokemon['type1'])
    # Fix Generation 0 to Generation 7
    pokemon.loc[pokemon['generation'] == 0, 'generation'] = 7
    # Split data into original and other forms
    original_forms = pokemon.drop_duplicates(subset="number", keep="first")
    other_forms = pokemon[pokemon.duplicated(subset="number", keep="first")]
    return original_forms, other_forms


def load(original_forms, other_forms, db_name='pokemon.db'):
    """Load Pokémon data into SQLite database."""
    print("Loading data into database...")
    conn = sqlite3.connect(db_name)
    # Write tables to SQLite database
    original_forms.to_sql('original_forms', conn, if_exists='replace', index=False)
    other_forms.to_sql('other_forms', conn, if_exists='replace', index=False)
    conn.close()
    print("Data successfully loaded into SQLite database.")


# Define a handler for file changes
class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path

    def on_modified(self, event):
        if event.src_path.endswith(self.file_path):
            print(f"Detected change in {self.file_path}. Running ETL...")
            pokemon = extract(self.file_path)
            original_forms, other_forms = transform(pokemon)
            load(original_forms, other_forms)


# Monitor the CSV file for changes
def monitor_file(file_path):
    print(f"Monitoring {file_path} for changes...")
    event_handler = FileChangeHandler(file_path)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        while True:
            print("Monitoring is active... Press Ctrl+C to stop.")
            time.sleep(10)  # Log a message every 10 seconds
    except KeyboardInterrupt:
        print("\nStopping monitoring...")
        observer.stop()
    observer.join()
    print("Monitoring stopped.")



# Run the monitor
if __name__ == "__main__":
    # Replace this with the actual path to your CSV file
    file_path = "Pokemon.csv"
    monitor_file(file_path)
