from rich.console import Console
from rich.table import Table
from .utils import read_expenses, write__to_expenses
from datetime import datetime

def list_expenses(filename=None):

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="magenta", justify="right", no_wrap=True)
    table.add_column("Date", justify="left")
    table.add_column("Description", style="red")
    table.add_column("Amount", justify="left", style="green")
    table.add_column("Category", justify="right", style="red")

    expenses = read_expenses()

    for expense in expenses:
        date = datetime.fromisoformat(expense['date']).strftime("%Y-%m-%d")
        amount = f"{expense['amount']:.2f}"
        table.add_row(
            str(expense['id']),
            date,
            expense['description'],
            f"{amount}",
            expense['category']
        )

    console.print(table)
