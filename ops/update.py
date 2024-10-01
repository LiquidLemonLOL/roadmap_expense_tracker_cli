from rich import print
from .utils import read_expenses, write__to_expenses

def update_expense(id, description, amount):

    expenses = read_expenses()
    if not expenses:
        print("[bold red]No expenses found.[bold red]")
        return
    
    for expense in expenses:
        if expense['id'] == id:
            expense['description'] = description if description is not None else expense['description']
            expense['amount'] = float(amount) if amount is not None else expense['amount']
        else:
            print(f"[bold red]No expense with ID {id} found.[bold red]")
            return
        
    write__to_expenses(expenses)
    print(f"Expense with ID {id} [bold green]updated.[bold green]")
