import inventory

inventory.add_item("Apfel", 10)
print("Bestand Apfel:", inventory.get_stock("Apfel"))

inventory.sell_item("Apfel", 1)
print("Bestand Apfel:", inventory.get_stock("Apfel"))

print("Gesamt:", inventory.total_items())
print("Gesamt:", inventory.total_items())
