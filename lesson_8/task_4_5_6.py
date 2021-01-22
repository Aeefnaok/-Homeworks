class OfficeEquipmentWarehouse:
    storage: dict = {}

    def __init__(self):
        pass

    def add_equipment(self, equipment, count):
        equipment_type = equipment.__class__.__name__
        try:
            self.storage[equipment_type][equipment.name] += count
        except KeyError:
            if equipment_type not in self.storage:
                self.storage[equipment_type] = {}
                self.storage[equipment_type][equipment.name] = count
            elif equipment.name not in self.storage[equipment_type]:
                self.storage[equipment_type][equipment.name] = count

    def __str__(self):
        output = ''
        for i, equipment in self.storage.items():
            output += f'{i}:\n'
            print(equipment)
            for j, count in equipment.items():
                output += f'\t{j} {count}\n'

        return output


class OfficeEquipment:
    name: str = None
    weight: float = float()
    __price: float = None

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        try:
            self.__price = float(price)
        except ValueError:
            print(f"price {price} is not a number")
            self.__price = None

    def __str__(self):
        return f'{self.name} {self.price} {self.weight}'


class Printer(OfficeEquipment):
    print_formats = ["A1", "A2", "A3", "A4", "A5"]
    print_format: str = None
    colored: bool = False

    def __init__(self, name, weight, price, print_format, colored):
        super(Printer, self).__init__(name, weight, price)
        self.print_format = print_format
        self.colored = colored

    def __str__(self):
        return '{name} {print_format} {colored} {price}руб {weight}кг' \
            .format(
            name=self.name,
            print_format=self.print_format,
            colored="colored" if self.colored else "monochrome",
            price=self.price,
            weight=self.weight
        )


class Scaner(OfficeEquipment):
    scan_formats = ["A1", "A2", "A3", "A4", "A5"]
    scan_format: str = None

    def __init__(self, name, weight, price, scan_format):
        super(Scaner, self).__init__(name, weight, price)
        self.scan_format = scan_format


class Xerox(OfficeEquipment):
    print_formats = ["A1", "A2", "A3", "A4", "A5"]
    scan_formats = ["A1", "A2", "A3", "A4", "A5"]
    print_format: str = None
    colored: bool = False
    scan_format: str = None

    def __init__(self, name, weight, price, print_format, colored, scan_format):
        super(Xerox, self).__init__(name, weight, price)
        self.print_format = print_format
        self.colored = colored
        self.scan_format = scan_format

    def __str__(self):
        return '{name} print {print_format} scan {scan_format} {colored} {price}руб {weight}кг' \
            .format(
            name=self.name,
            print_format=self.print_format,
            scan_format=self.scan_format,
            colored="colored" if self.colored else "monochrome",
            price=self.price,
            weight=self.weight
        )


if __name__ == '__main__':
    storage = OfficeEquipmentWarehouse()
    of_eq = OfficeEquipment("01", 1, "4000")
    print1 = Printer(
        name="print1",
        weight=3,
        price="8000",
        print_format="A4",
        colored=True
    )
    scan1 = Scaner(
        "scan1",
        weight=1,
        price="4000",
        scan_format="A4",

    )
    scan2 = Scaner(
        "scan2",
        weight=2,
        price="5500",
        scan_format="A3",

    )
    xer1 = Xerox(
        name="xer1",
        weight=7,
        price="21000",
        print_format="A4",
        colored=True,
        scan_format="A4"
    )
    print(of_eq)
    print(xer1)
    print(print1)
    print(scan1)
    print(scan2)
    storage.add_equipment(print1, 5)
    storage.add_equipment(print1, 2)
    storage.add_equipment(scan1, 6)
    storage.add_equipment(scan2, 2)
    storage.add_equipment(xer1, 2)
    print(storage)

