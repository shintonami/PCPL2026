"""РК-1, вариант Г-20. Доронкин Артём Сергеевич, ИУ5-35Б."""
from operator import itemgetter


class Part:
    """Деталь: идентификатор, название, цена в рублях, поставщик."""
    def __init__(self, id, name, price, supplier_id):
        self.id = id
        self.name = name
        self.price = price
        self.supplier_id = supplier_id


class Supplier:
    """Поставщик."""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PartSupplier:
    """Связь детали и поставщика многие-ко-многим."""
    def __init__(self, part_id, supplier_id):
        self.part_id = part_id
        self.supplier_id = supplier_id


suppliers = [
    Supplier(1, 'Альфа'),
    Supplier(2, 'Вектор'),
    Supplier(3, 'Атлас'),
]

parts = [
    Part(1, 'Болт', 20, 1),
    Part(2, 'Гайка', 10, 1),
    Part(3, 'Подшипник', 500, 2),
    Part(4, 'Шестерня', 800, 2),
    Part(5, 'Вал', 1200, 3),
]

# Болт поставляют Альфа и Атлас Альфа поставляет Болт и Гайку.
parts_suppliers = [
    PartSupplier(1, 1),
    PartSupplier(2, 1),
    PartSupplier(3, 2),
    PartSupplier(5, 3),
    PartSupplier(1, 3),
]


def query_g1(parts, suppliers):
    """Поставщики на А и их детали (один-ко-многим)."""
    return [
        (s.name, [p.name for p in parts if p.supplier_id == s.id])
        for s in suppliers if s.name.startswith('А')
    ]


def query_g2(parts, suppliers):
    """Максимальные цены по поставщикам, по убыванию."""
    maxima = [
        (s.name, max(p.price for p in parts if p.supplier_id == s.id))
        for s in suppliers
        if any(p.supplier_id == s.id for p in parts)
    ]
    return sorted(maxima, key=itemgetter(1), reverse=True)


def query_g3(parts, suppliers, links):
    """Все связанные пары многие-ко-многим, по поставщику."""
    pairs = [
        (p.name, s.name)
        for link in links
        for p in parts if p.id == link.part_id
        for s in suppliers if s.id == link.supplier_id
    ]
    return sorted(pairs, key=itemgetter(1))


def main():
    print('Г1. Поставщики на А и их детали (один-ко-многим):')
    for supplier, names in query_g1(parts, suppliers):
        print(f'{supplier}: {", ".join(names)}')

    print('\nГ2. Максимальная цена детали (по убыванию):')
    for supplier, price in query_g2(parts, suppliers):
        print(f'{supplier}: {price} руб.')

    print('\nГ3. Деталь - поставщик (многие-ко-многим):')
    for part, supplier in query_g3(parts, suppliers, parts_suppliers):
        print(f'{part} - {supplier}')


if __name__ == '__main__':
    main()
