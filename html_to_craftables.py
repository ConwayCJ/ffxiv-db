import requests
from bs4 import BeautifulSoup

professions = ["Carpenter", "Blacksmith", "Armorer", "Goldsmith", "Leatherworker", "Weaver", "Alchemist", "Culinarian"]
tiers = ["1_-_9", "10_-_19", "20_-_29", "30_-_39", "40_-_49", "50","51_-_59", "60", "61_-_69", "70", "71_-_79", "80", "81_-_89", "90"]

class Craftable:
  def __init__(self, name, profession, png, lvl, type, _yield, dur, diff, max_qual, ingredients):
    self.name = name
    self.profession = profession
    self.png = png
    self.lvl = lvl
    self.type = type
    self._yield = _yield
    self.dur = dur
    self.diff = diff
    self.max_qual = max_qual
    self.ingredients = ingredients
  
  def vals_to_list(self):
    ingredients_list = [[ingredient.name, ingredient.quantity] for ingredient in self.ingredients]
    return [self.name, self.profession, self.png, self.lvl, self.type, self._yield, self.dur, self.diff, self.max_qual, ingredients_list]


class Ingredient:
  def __init__(self, name, quantity):
    self.name = name
    self.quantity = quantity

def parse_all_pages():
  all_craftables = {}

  for prof in professions:

    if prof not in all_craftables:
      all_craftables[prof] = {}

    for tier in tiers:
      rows = parse_page(prof, tier)

      all_craftables[prof][tier] = rows_to_craftables(rows)

  print(all_craftables)
  return all_craftables

def parse_page(profession, tier):
    if not isinstance(tier, str):
      tier = str(tier)

    if "_-_" not in tier:
      tier = tier.replace("-", "_-_")

    url = 'https://ffxiv.consolegameswiki.com/wiki/{}_Recipes/Level_{}'.format(profession, tier)
    page = requests.get(url)

    if page.status_code == 404:
      raise requests.exceptions.HTTPError("Issue connecting to wiki. Try a valid range. Here's a list\n1-9, 10-19, 20-29, 30-39, 40-49, 50,\n51-59, 60, 61-69, 70, 71-79, 80, 81-89, 90")

    soup = BeautifulSoup(page.content, 'html.parser')
  
    tbody = soup.find("tbody")
    rows = tbody.find_all("tr")
    thead = rows.pop(0)

    return rows

def rows_to_craftables(rows):
  craftables = []
  for item in rows:
    craftable = row_to_craftable(item)
    craftables.append(craftable)
    
  return craftables

def row_to_craftable(row):
    cols = row.find_all("td")

    # name / png
    col_1 = cols.pop(0)
    c_name = col_1.get_text(strip=True)
    png = 'https://ffxiv.consolegameswiki.com' + col_1.find('img')['src']
    
    if "'" in c_name:
      c_name = c_name.replace("'", r"\'")

    # profession
    prof = cols.pop(0).find("a").get_text(strip=True)
    # lvl
    lvl = cols.pop(0).get_text(strip=True)

    if "★" in lvl:
      lvl = lvl.replace("★","*")
    # type
    type = cols.pop(0).get_text(strip=True).replace("'", r"\'")
    # yield
    _yield = cols.pop(0).get_text(strip=True)
    # durability
    dur = int(cols.pop(0).get_text(strip=True))
    # difficulty
    diff = int(cols.pop(0).get_text(strip=True))
    # max_qual
    max_qual = int(cols.pop(0).get_text(strip=True))
    #ingredients
    ing_col = cols.pop(0).find("dl")
    ingredients = []

    ing_quants = ing_col.find_all("dt")
    ing_names = ing_col.find_all("dd")

    for name, quantity in zip(ing_names, ing_quants):
      name = name.find_all("a")[-1].get_text()
      quantity = quantity.get_text()

      if "'" in name : 
        name = name.replace("'", r"\'")
  
      ingredients.append(Ingredient(name, quantity))

    return Craftable(c_name, png, prof, lvl, type, _yield, dur, diff, max_qual, ingredients)
