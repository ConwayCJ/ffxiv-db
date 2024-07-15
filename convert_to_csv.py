from html_to_craftables import parse_all_pages, parse_page, rows_to_craftables, row_to_craftable
from html_to_craftables import Craftable, Ingredient, professions, tiers
import csv

# doesn't use a dict
def make_profession_csv(prof): 

  header = ["name", "profession", "png", "lvl", "type", "yield", "dur", "diff", "max_qual", "ingredients", "range"]
  file_name = prof + "_db.csv"

  prof_dict = {}

  for tier in tiers:
    tier = tier.replace('_-_', '-')

    html = parse_page(prof, tier)
    prof_dict[tier] = rows_to_craftables(html)
    
  with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    # write header
    writer.writerow(header)

    for range in prof_dict:
      for craftable in prof_dict[range]:
        vals = craftable.vals_to_list()
        print(vals)
        writer.writerow(vals + [range])