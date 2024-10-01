from rich import print
from .utils import read_expenses, write__to_expenses

def delete_from_expenses(id):

    expenses = read_expenses()
    if not expenses:
        print("[bold red]No expenses found.[bold red]")
        return
    
    if not any(expense['id'] == id for expense in expenses):
        print(f"[bold red]No expense with ID {id} found.[bold red]")
        return
    
    expenses = [expense for expense in expenses if expense['id'] != id]
    write__to_expenses(expenses)
    print(f"Expense with ID {id} [bold red]deleted.[/bold red]")