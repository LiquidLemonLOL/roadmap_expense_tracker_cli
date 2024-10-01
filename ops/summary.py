from rich.console import Console
from rich.table import Table
from .utils import read_expenses, get_month_name
from datetime import datetime

def expense_summary(month):

    expenses = read_expenses()
    if not expenses:
        print("[bold red]No expenses found.[bold red]")
        return
    
    month_print = ""
    if month:
        expenses = [expense for expense in expenses if datetime.fromisoformat(expense['date']).month == month]
        month_print = f"for month of {get_month_name(month)}"
    
    total_expense = sum(expense['amount'] for expense in expenses)

    console = Console()
    console.print(f"[bold red]Expense summary[bold red] {month_print}")
    console.print(f"[bold green]{total_expense}[bold green]")


