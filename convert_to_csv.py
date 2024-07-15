from html_to_craftables import parse_all_pages, parse_page, rows_to_craftables, row_to_craftable
from html_to_craftables import Craftable, Ingredient, professions, tiers
import csv
import os

def make_crafter_db_csv():
  header = ["name", "profession", "png", "lvl", "type", "yield", "dur", "diff", "max_qual", "ingredients", "range"]

  folder_path = './crafter_csvs/'
  os.makedirs(folder_path, exist_ok=True)

  csv_path = os.path.join(folder_path, 'all_crafters.csv')

  with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)

    # write header
    writer.writerow(header)
    dict = parse_all_pages()
    
    # each profession
    for prof in dict:
    # each range
      for range in dict[prof]:
    # each craftable
        for item in dict[prof][range]:
          print(item)
          vals = item.vals_to_list()
          writer.writerow(vals + [range])

def make_profession_csv(prof):

  header = ["name", "profession", "png", "lvl", "type", "yield", "dur", "diff", "max_qual", "ingredients", "range"]
  file_name = prof.lower() + "_db.csv"

  folder_path = './crafter_csvs/'
  os.makedirs(folder_path, exist_ok=True)

  prof_dict = {}

  for tier in tiers:
    tier = tier.replace('_-_', '-')

    html = parse_page(prof, tier)
    prof_dict[tier] = rows_to_craftables(html)

  csv_file_path = os.path.join(folder_path + file_name)  
  with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    # write header
    writer.writerow(header)

    for range in prof_dict:
      for craftable in prof_dict[range]:
        vals = craftable.vals_to_list()
        print(vals)
        writer.writerow(vals + [range])