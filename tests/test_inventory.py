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
        for name in [123]:
            for qty in [5]:
                with self.assertRaises(ValueError) as cm:
                    inventory.add_item(name, qty)
        self.assertEqual(str(cm.exception), f"Fehler: Artikelname '{name}' muss ein String sein.")

    def test_add_item_falsche_menge(self):
        inventory.add_item("Weintrauben", 10)
        for name in ["Weintrauben"]:
            for qty in ["fünf"]:
                with self.assertRaises(ValueError) as cm:
                    inventory.add_item(name, qty)
        self.assertEqual(str(cm.exception), "Fehler: Menge 'fünf' muss eine Zahl sein.")

    def test_sell_item_gueltig(self):
        inventory.add_item("Banane", 5)
        inventory.sell_item("Banane", 3)
        self.assertEqual(inventory.items["Banane"], 2)

    def test_sell_item_ungueltiger_zahl(self):
        inventory.add_item("Apfel", 10)
        for name in ["Apfel"]:
            for qty in ["Hallo"]:
                with self.assertRaises(ValueError) as cm:
                    inventory.sell_item(name, qty)
        self.assertEqual(str(cm.exception), "Fehler: Menge 'Hallo' muss eine Zahl sein.")

    def test_sell_item_ungueltiger_name(self):
        inventory.add_item("Apfel", 10)
        for name in [5]:
            for qty in [10]:
                with self.assertRaises(ValueError) as cm:
                    inventory.sell_item(name, qty)
        self.assertEqual(str(cm.exception), f"Fehler: Artikelname '{name}' muss ein String sein.")

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
        for name in [123]:
            with self.assertRaises(ValueError) as cm:
                inventory.get_stock(name)
            self.assertEqual(str(cm.exception), f"Fehler: '{name}', der Artikelname muss ein String sein.")

    def test_get_stock_artikel_existiert_nicht(self):
        inventory.add_item("Apfel", 10)
        for name in ["Birne"]:
            with self.assertRaises(ValueError) as cm:
                inventory.get_stock(name)
            self.assertEqual(str(cm.exception), f"Fehler: Artikel '{name}' existiert nicht im Lager.")

    def test_total_items_und_sell_items(self):
        inventory.add_item("Apfel", 5)
        inventory.add_item("Banane", 10)
        inventory.sell_item("Apfel", 1)
        self.assertEqual(inventory.total_items(), 14)
