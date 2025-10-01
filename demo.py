import inventory

inventory.add_item("Apfel", 1)
inventory.add_item("Bananen", 10)
inventory.add_item("Weintrauben", 10)
inventory.add_item("Birnen", 5)

print("Bestand Apfel:", inventory.get_stock("Apfel"))
print("Bestand Bananen:", inventory.get_stock("Bananen"))
print("Bestand Birnen:", inventory.get_stock("Birnen"))
print("Bestand Weintrauben:", inventory.get_stock("Weintrauben"))

inventory.sell_item("Weintrauben", 4)
inventory.sell_item("Apfel", 1)
inventory.sell_item("Bananen", 5)
inventory.sell_item("Birnen", 4)

try:
    print("Bestand Apfel nach Verkauf:", inventory.get_stock("Apfel"))
except ValueError:
    print("Apfel ist nicht mehr im Lager.")
print("Bestand Bananen nach Verkauf:", inventory.get_stock("Bananen"))
print("Bestand Weintrauben nach Verkauf:", inventory.get_stock("Weintrauben"))
print("Bestand Birnen nach Verkauf:", inventory.get_stock("Birnen"))

print("Gesamtanzahl der Waren:", inventory.total_items())
