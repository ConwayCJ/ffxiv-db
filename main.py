import argparse, sys
from html_to_craftables import parse_page, parse_all_pages

def main():
  parser = argparse.ArgumentParser(description="TLDR: Command line tool for multiple tasks such as parsing the ffxiv wikipedia to convert tables to CSV files.")

  subparsers = parser.add_subparsers(dest="command", help="AVAILABLE COMMANDS")

  # SINGLE ARG COMMANDS
  subparsers.add_parser('new-craft-db', help='Converts ffxiv wikipedia to CSV files for each profession.')
  subparsers.add_parser('list-professions', help="1-9, 10-19, 20-29, 30-39, 40-49, 50,\n51-59, 60, 61-69, 70, 71-79, 80, 81-89, 90")
  
  # MULTIPLE ARG COMMANDS
  comm_parse_page = subparsers.add_parser('profession-to-csv',)
  comm_parse_page.add_argument('profession', type=str, help='Name of the profession')
  comm_parse_page.add_argument('tier', type=str, help='Tier range, e.g. "1-9". Try: <main.py list-professions> for list of options')
  

  args = parser.parse_args()
  # command list
  if args.command == 'help' or args.command is None:
     parser.print_help()
  elif args.command =='list-professions':
     print("""
          PROFESSIONS: Carpenter, Blacksmith, Armorer, Goldsmith, Leatherworker, Weaver, Alchemist, Culinarian
          RANGES: 1-9, 10-19, 20-29, 30-39, 40-49, 50, 51-59, 60, 61-69, 70, 71-79, 80, 81-89, 90""")
  # more commands
     
# END
if __name__ == "__main__":
    main()