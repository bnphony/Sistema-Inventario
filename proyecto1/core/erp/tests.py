import os

from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
setup()


import random

from core.erp.models import *

print('hola desde la app')
from django.db import connection
from django.test import TestCase


class CategoryModelTest(TestCase):
    def setUp(self):
        # Imprimir a que base de datos se esta conectando
        print("Database name:", connection.settings_dict['NAME'])
        self.category = Category.objects.create(name="Electronics", desc="Electronic items")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.desc, "Electronic items")

    def test_category_str_method(self):
        self.assertEqual(str(self.category), "Nombre: Electronics")



# data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
#         'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
#         'Grasas, aceite y mantequilla']


# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#            'u', 'v', 'w', 'x', 'y', 'z']

# for i in range(1, 60):
#     name = ''.join(random.choices(letters, k=5))
#     while Category.objects.filter(name=name).exists():
#         name = ''.join(random.choices(letters, k=5))
#     # Category(name=name).save()
#     print('Guardado registro {}'.format(i))



# for i in data:
#     cat = Category(name=i)
#     cat.save()
#     print('Guardado registro N°{}'.format(cat.id))
