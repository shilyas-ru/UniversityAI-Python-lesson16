"""
Задание:

1. Написать тесты для проекта с помощью pytest или unittest

Тесты будут написаны на unittest.

Ссылка на документацию:
https://docs.python.org/3/library/unittest.html
"""

import unittest

from lesson15_lotto_game import Bag, Card


class TestClassBag(unittest.TestCase):

    def setUp(self):
        self.bag_of_barrels = Bag()

    def test_Bag_init(self):
        self.assertEqual(len(self.bag_of_barrels.barrels_in_bag), 90)

    def test_Bag_shuffle_barrels(self):
        # Сохраняем исходный список
        init_bag_of_barrels = self.bag_of_barrels.barrels_in_bag[:]
        # Перемешиваем
        self.bag_of_barrels.shuffle_barrels()
        # Проверяем, что исходный список не равен перемешанному
        self.assertNotEqual(init_bag_of_barrels, self.bag_of_barrels.barrels_in_bag)
        # Сортируем оба списка по возрастанию и проверяем, что они равны
        self.assertListEqual(sorted(init_bag_of_barrels), sorted(self.bag_of_barrels.barrels_in_bag))

    def test_Bag_get_barrel(self):
        # Сохраняем исходный список
        init_bag_of_barrels = self.bag_of_barrels.barrels_in_bag[:]
        # Получили номер из мешка
        barrel_num = self.bag_of_barrels.get_barrel()
        # Проверяем, что список уменьшился на единицу
        self.assertEqual(len(self.bag_of_barrels.barrels_in_bag), 89)

        # проверяем, что такой номер в исходном списке имеется
        self.assertIn(barrel_num, init_bag_of_barrels)
        # проверяем, что такой номер в списке отсутствует - то
        # есть, номер был удалён при выборе
        self.assertNotIn(barrel_num, self.bag_of_barrels.barrels_in_bag)

        # Проверяем, что полученный из мешка номер больше 0 и меньше 90
        self.assertGreater(barrel_num, 0)
        self.assertLessEqual(barrel_num, 90)

    def test_Bag_remaining_barrels_num(self):
        self.assertEqual(len(self.bag_of_barrels.barrels_in_bag), 90)
        # Получили номер из мешка
        barrel_num = self.bag_of_barrels.get_barrel()
        # Проверяем, что список уменьшился на единицу
        self.assertEqual(len(self.bag_of_barrels.barrels_in_bag), 89)


class TestClassCard(unittest.TestCase):

    def setUp(self):
        self.player_card = Card()

    def test_Card_init(self):
        self.assertListEqual(self.player_card.init_card, self.player_card.card)

    def test_Card_find_num(self):
        for num in range(1, 91):
            if num not in self.player_card.card:
                break
        # num - это номер, отсутствующий в списке
        # Функция должна вернуть -1
        self.assertEqual(self.player_card.find_num(num), -1)
        # self.player_card.card[0] - это номер, имеющийся в списке
        # Функция должна вернуть 0
        self.assertEqual(self.player_card.find_num(self.player_card.card[0]), 0)

    def test_Card_del_num(self):
        # Сохраняем исходный список
        init_bag_of_barrels = self.player_card.card[:]

        # Проверяем, что при удалении отсутствующего элемента - список не меняется
        self.player_card.del_num(2, 91)  # 2: Удалить элемент по значению
        self.assertListEqual(init_bag_of_barrels, self.player_card.card)

        # num - это номер, имеющийся в списке
        for num in range(1, 91):
            if num in self.player_card.card:
                break
        idx = self.player_card.find_num(num)
        self.player_card.del_num(2, num)  # 2: Удалить элемент по значению
        # Проверяем, что исходный список не равен списку с удалённым элементом.
        self.assertNotEqual(init_bag_of_barrels, self.player_card.card)
        # Проверяем, что записывается вместо удалённого элемента значение -1
        init_bag_of_barrels[idx] = -1
        self.assertListEqual(init_bag_of_barrels, self.player_card.card)

        # Сохраняем заново исходный список, так как был удалён элемент
        init_bag_of_barrels = self.player_card.card[:]
        # num - это номер, имеющийся в списке
        for num in range(1, 91):
            if num in self.player_card.card:
                break
        idx = self.player_card.find_num(num)
        self.player_card.del_num(1, idx)  # 1: Удалить элемент по индексу
        # Проверяем, что исходный список не равен списку с удалённым элементом.
        self.assertNotEqual(init_bag_of_barrels, self.player_card.card)
        # Проверяем, что записывается вместо удалённого элемента значение -1
        init_bag_of_barrels[idx] = -1
        self.assertListEqual(init_bag_of_barrels, self.player_card.card)

    def test_Card_empty_card(self):
        # Сохраняем исходный список
        # Карточка не пустая. Возвращается False.
        self.assertFalse(self.player_card.empty_card())
        # Формируем карточку, в которой все ячейки с цифрами как бы "зачёркнуты"
        for i in range(len(self.player_card.card)):
            if self.player_card.card[i] > 0:
                self.player_card.card[i] = -1
        # Карточка не пустая. Возвращается True.
        self.assertTrue(self.player_card.empty_card())


if __name__ == '__main__':
    unittest.main()
