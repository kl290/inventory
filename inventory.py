# Globale Datenstruktur für das Lager
items = {}  # key: Artikelname, value: Anzahl

def add_item(name, qty):
    if name in items:
        items[name] = items[name] + qty
    else:
        items[name] = qty
    return True

def sell_item(name, qty):
    if name not in items:
        return False
    items[name] = items[name] - qty
    return True

def get_stock(name):
    return items.get(name)

def total_items():
    return len(items)
