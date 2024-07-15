import requests
from bs4 import BeautifulSoup

types = ["Carpenter", "Blacksmith", "Armorer", "Goldsmith", "Leatherworker", "Weaver", "Alchemist", "Culinarian"]
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

class Ingredient:
  def __init__(self, name, quantity):
    self.name = name
    self.quantity = quantity


def parse_page(profession, tier):
    # for profession in types:
    #   for tier in tiers:
    if "-" in tier:
      tier = tier.replace("-", "_-_")

    # url = 'https://ffxiv.consolegameswiki.com/wiki/{}_Recipes/Level_{}'.format(profession,tier)
    url = 'https://ffxiv.consolegameswiki.com/wiki/{}_Recipes/Level_{}'.format(profession, tier)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    tbl = soup.find("tbody")
    rows = tbl.find_all("tr")
    header = rows.pop(0)
    items = rows

    craftables = []

    for item in items:
      craftable = tbl_row_to_craftable(item)
      craftables.append(craftable)
    
    print(craftables)
    return craftables

def tbl_row_to_craftable(row):
    cols = row.find_all("td")

    # name / png
    col_1 = cols.pop(0)
    name = col_1.get_text()
    png = 'https://ffxiv.consolegameswiki.com' + col_1.find('img')['src']
    
    if "'" in name:
      name = name.replace("'", r"\'")

    # profession
    prof = cols.pop(0).find("a").get_text(strip=True)
    # lvl
    lvl = cols.pop(0).get_text(strip=True)
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

    return Craftable(name,png, prof, lvl, type, _yield, dur, diff, max_qual, ingredients)
