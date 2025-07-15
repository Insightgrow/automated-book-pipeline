import csv
from tabulate import tabulate

def display_dashboard():
    with open("logs.csv", newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        table = list(reader)

    print("\nAutomated Book Pipeline Dashboard\n")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))  # Terminal display

    with open("dashboard.md", "w", encoding="utf-8") as f:
        f.write("# Automated Book Pipeline Dashboard\n\n")
        f.write(tabulate(table, headers=headers, tablefmt="github"))

    print("\nDashboard also saved as 'dashboard.md' in GitHub-friendly Markdown format.\n")

if __name__ == "__main__":
    display_dashboard()
