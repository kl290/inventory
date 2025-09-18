import inventory

inventory.add_item("Apfel", 10)
inventory.add_item("Bananen", 10)
inventory.add_item("Weintrauben", 10)
inventory.add_item("Birnen", 4)

print("Bestand Apfel:", inventory.get_stock("Apfel"))
print("Bestand Bananen:", inventory.get_stock("Bananen"))
print("Bestand Birnen:", inventory.get_stock("Birnen"))
print("Bestand Weintrauben:", inventory.get_stock("Weintrauben"))

inventory.sell_item("Weintrauben", "Hallo")
inventory.sell_item("Apfel", 1)
inventory.sell_item("Bananen", 5)
inventory.sell_item("Birnen", 4)

print("Bestand Apfel nach Verkauf:", inventory.get_stock("Apfel"))
print("Bestand Bananen nach Verkauf:", inventory.get_stock("Bananen"))
print("Bestand Weintrauben nach Verkauf:", inventory.get_stock("Weintrauben"))
print("Bestand Birnen nach Verkauf:", inventory.get_stock("Birnen"))

print("Gesamtanzahl der Waren:", inventory.total_items())
