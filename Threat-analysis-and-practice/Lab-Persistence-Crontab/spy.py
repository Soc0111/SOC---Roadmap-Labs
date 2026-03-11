import datetime
import os

# Имитация работы шпионского ПО: запись логов в скрытый файл
log_path = os.path.expanduser("~/hidden_spy_log.txt")

def simulate_spy_activity():
    with open(log_path, "a") as f:
        f.write(f"Spy process active. Timestamp: {datetime.datetime.now()}\n")

if __name__ == "__main__":
    simulate_spy_activity()
