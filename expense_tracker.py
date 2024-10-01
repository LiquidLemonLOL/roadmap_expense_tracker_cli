import json
import rich
from rich.console import Console
from rich.table import Table
import argparse
from ops.add import add_to_expenses
from ops.delete import delete_from_expenses
from ops.update import update_expense
from ops.list import list_expenses
from ops.summary import expense_summary
from ops.utils import json_to_csv

#init main parser + subparser
parser = argparse.ArgumentParser(description="Expense Tracker to keep track of how spend your money!")
subparsers = parser.add_subparsers(dest= 'sub', help="Sub-commands")

#add each subparser (add, delete, update, list, summary)
subparser_add = subparsers.add_parser('add', help="Adds a new expense with specified description, amount and category.")
subparser_add.add_argument('--description', required=True, type=str, help="Description of the expense")
subparser_add.add_argument('--amount', required=True, type=float, help="Amount of the expense")
subparser_add.add_argument('--category', type=str, required=False, nargs='?', default="", help="Category of the expense")

subparser_delete = subparsers.add_parser('delete', help="Deletes an existing expense based on ID")
subparser_delete.add_argument('--id', type=int, help="ID for the expense to delete")

subparser_update = subparsers.add_parser('update', help="Updates an existing expense based on id with a new description and amount.")
subparser_update.add_argument('--id', type=int, required=True, help="ID of expense to update")
subparser_update.add_argument('--description', required=False, help="New description for expense (optional)")
subparser_update.add_argument('--amount', required=False, help="New amount for expense (optional)")

subparser_list = subparsers.add_parser('list', help="Displays list of all expenses")

subparser_export = subparsers.add_parser('export', help="Exports all expenses into a CSV file")

subparser_summary = subparsers.add_parser('summary', help="Shows summary of total amount of expenses")
subparser_summary.add_argument('--month', type=int, help="Shows expense summary for month number")

#parse user args and match for function
args = parser.parse_args()

match args.sub:
    case 'add':
        add_to_expenses(args.description, args.amount, args.category)
    case 'delete':
        delete_from_expenses(args.id)
    case 'update':
        update_expense(args.id, args.description, args.amount)
    case 'list':
        list_expenses()
    case 'summary':
        expense_summary(args.month)
    case 'export':
        json_to_csv()
    case _:
        parser.print_help()
