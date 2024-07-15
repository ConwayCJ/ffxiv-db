import argparse, sys
from html_to_craftables import parse_page, parse_all_pages
from convert_to_csv import make_crafter_db_csv, make_profession_csv

def main():
  parser = argparse.ArgumentParser(description="TLDR: Command line tool for multiple tasks such as parsing the ffxiv wikipedia to convert tables to csv files.")

  subparsers = parser.add_subparsers(dest="command", help="AVAILABLE COMMANDS")

  # SINGLE ARG COMMANDS
  subparsers.add_parser('new-craft-db', help='Converts ffxiv wikipedia to CSV files for each profession.')
  subparsers.add_parser('list-professions', help="1-9, 10-19, 20-29, 30-39, 40-49, 50,\n51-59, 60, 61-69, 70, 71-79, 80, 81-89, 90")
  subparsers.add_parser('make-crafter-csv', help="Parses the ffxiv wikipedia and converts every professions craftable items a single csv file")

  # MULTIPLE ARG COMMANDS
  comm_parse_page = subparsers.add_parser('make-profession-csv', help="Parses the ffxiv wikipedia and converts a single professios craftable items to a single csv file. e.g. <main.py make-profession-csv blacksmith>")
  comm_parse_page.add_argument('profession', type=str, help='Name of the profession')  

  args = parser.parse_args()
  # command list
  if args.command == 'help' or args.command is None:
     parser.print_help()
  elif args.command == 'list-professions':
     print("""
          PROFESSIONS: Carpenter, Blacksmith, Armorer, Goldsmith, Leatherworker, Weaver, Alchemist, Culinarian
          RANGES: 1-9, 10-19, 20-29, 30-39, 40-49, 50, 51-59, 60, 61-69, 70, 71-79, 80, 81-89, 90""")
  elif args.command == 'make-crafter-csv':
     make_crafter_db_csv()
  elif args.command == 'make-profession-csv':
     make_profession_csv(args.profession)
     
  
  # more commands
     
# END
if __name__ == "__main__":
    main()