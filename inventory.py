# Globale Datenstruktur für das Lager
items = {}  # key: Artikelname, value: Anzahl


def add_item(name, qty):
    if not isinstance(name, str):
        raise ValueError(f"Fehler: Artikelname '{name}' muss ein String sein.")
    if not isinstance(qty, int):
        raise ValueError(f"Fehler: Menge '{qty}' muss eine Zahl sein.")

    if name in items:
        items[name] += qty
    else:
        items[name] = qty
    return True


def sell_item(name, qty):
    if not isinstance(name, str):
        raise ValueError(f"Fehler: Artikelname '{name}' muss ein String sein.")
    if not isinstance(qty, int):
        raise ValueError(f"Fehler: Menge '{qty}' muss eine Zahl sein.")
    if name not in items:
        raise ValueError(f"Fehler: Artikel '{name}' existiert nicht im Lager.")
    if items[name] < qty:
        raise ValueError(f"Fehler: '{name}' können nicht verkauft werden, Bestand zu niedrig.")

    items[name] -= qty
    return True


def get_stock(name):
    if not isinstance(name, str):
        raise ValueError(f"Fehler: '{name}', der Artikelname muss ein String sein.")
    if name not in items:
        raise ValueError(f"Fehler: Artikel '{name}' existiert nicht im Lager.")
    return items[name]


def total_items():
    return sum(items.values())
