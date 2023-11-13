import csv

def save_birthday(name: str, date: str):
    """
    append row to events.csv.
    
    name: frst name + surname
    
    date: YYYY-MM-DD
    """
    with open('events.csv','a', encoding="utf8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name,date,"dirthday"])