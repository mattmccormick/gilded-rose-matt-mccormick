

class Item(object):
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def purchase(self):
        return True

    @staticmethod
    def get_all():
        return {
            1: Item(1, 'Chair', 'Ergonomic chair', 100),
            2: Item(2, 'Desk', 'Standing/sitting desk', 200),
            3: Item(3, 'Lamp', 'Desk lamp', 20),
            4: Item(4, 'Lock', 'Padlock with combination', 5),
            5: Item(5, 'Pen', 'Classy ball point pen', 20)
        }

    @staticmethod
    def get(id):
        items = Item.get_all()
        return items[id]