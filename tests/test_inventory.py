import unittest

import inventory


class TestInventar(unittest.TestCase):

    def setUp(self):
        inventory.items.clear()

    def test_add_item_und_get_stock(self):
        inventory.add_item("Apfel", 10)
        self.assertEqual(inventory.items["Apfel"], 10)

    def test_add_item_return_true(self):
        result = inventory.add_item("Apfel", 10)
        self.assertTrue(result)
        self.assertEqual(inventory.items["Apfel"], 10)

    def test_add_item_existing_item_erhoeht_bestand(self):
        inventory.add_item("Apfel", 5)
        self.assertEqual(inventory.items["Apfel"], 5)

        inventory.add_item("Apfel", 3)
        self.assertEqual(inventory.items["Apfel"], 8)

    def test_add_item_falscher_name(self):
        inventory.add_item("Apfel", 5)
        with self.assertRaises(ValueError) as cm:
            inventory.add_item(123, 5)
        self.assertEqual(str(cm.exception), "Fehler: Artikelname '123' muss ein String sein.")

    def test_add_item_leerer_string(self):
        with self.assertRaises(ValueError) as cm:
            inventory.add_item(" ", 5)
        self.assertEqual(str(cm.exception),
                         "Fehler: Artikelname darf nicht leer sein oder nur aus Leerzeichen bestehen.")

    def test_add_item_menge_0(self):
        with self.assertRaises(ValueError) as cm:
            inventory.add_item("Äpfel", 0)
        self.assertEqual(str(cm.exception), "Fehler: Die Menge muss größer als 0 sein.")

    def test_add_item_falsche_menge(self):
        inventory.add_item("Weintrauben", 10)
        with self.assertRaises(ValueError) as cm:
            inventory.add_item("Weintrauben", "fünf")
        self.assertEqual(str(cm.exception), "Fehler: Die Menge muss eine Zahl sein.")

    def test_sell_item_gueltig(self):
        inventory.add_item("Banane", 5)
        inventory.sell_item("Banane", 3)
        self.assertEqual(inventory.items["Banane"], 2)

    def test_sell_item_ungueltiger_zahl(self):
        inventory.add_item("Apfel", 10)
        with self.assertRaises(ValueError) as cm:
            inventory.sell_item("Apfel", "Hallo")
        self.assertEqual(str(cm.exception), "Fehler: Menge 'Hallo' muss eine Zahl sein.")

    def test_sell_item_ungueltiger_name(self):
        inventory.add_item("Apfel", 10)
        with self.assertRaises(ValueError) as cm:
            inventory.sell_item(5, 10)
        self.assertEqual(str(cm.exception), "Fehler: Artikelname '5' muss ein String sein.")

    def test_sell_item_return_true(self):
        inventory.add_item("Banane", 10)
        result = inventory.sell_item("Banane", 3)
        self.assertTrue(result)
        self.assertEqual(inventory.items["Banane"], 7)

    def test_sell_item_groesser_als_add_item(self):
        inventory.add_item("Apfel", 3)
        with self.assertRaises(ValueError) as cm:
            inventory.sell_item("Apfel", 5)
        self.assertEqual(str(cm.exception), "Fehler: 'Apfel' können nicht verkauft werden, Bestand zu niedrig.")
        self.assertEqual(inventory.items["Apfel"], 3)

    def test_sell_item_artikel_existiert_nicht(self):
        with self.assertRaises(ValueError) as cm:
            inventory.sell_item("Birne", 1)
        self.assertEqual(str(cm.exception), "Fehler: Artikel 'Birne' existiert nicht im Lager.")

    def test_get_stock_falscher_datentyp(self):
        inventory.add_item("Apfel", 10)
        with self.assertRaises(ValueError) as cm:
            inventory.get_stock(123)
        self.assertEqual(str(cm.exception), "Fehler: '123', der Artikelname muss ein String sein.")

    def test_get_stock_artikel_existiert_nicht(self):
        inventory.add_item("Apfel", 10)
        with self.assertRaises(ValueError) as cm:
            inventory.get_stock("Birne")
        self.assertEqual(str(cm.exception), "Fehler: Artikel 'Birne' existiert nicht im Lager.")

    def test_total_items_und_sell_items(self):
        inventory.add_item("Apfel", 5)
        inventory.add_item("Banane", 10)
        inventory.sell_item("Apfel", 1)
        self.assertEqual(inventory.total_items(), 14)

    def test_item_aus_liste_bei_bestand_0(self):
        inventory.add_item("Apfel", 5)
        inventory.sell_item("Apfel", 5)
        self.assertNotIn("Apfel", inventory.items)
