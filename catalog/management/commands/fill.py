from django.core.management import BaseCommand
from catalog.models import Category, Product
from config_root import root_path
import os
import json

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open(os.path.join(root_path, 'catalog.json'), 'r', encoding='utf-8') as r_file:
            raw_json = r_file.read()
            obj = json.loads(raw_json)
            new_obj = list(filter(lambda x: x['model'] == 'catalog.category', obj))
        return new_obj


    @staticmethod
    def json_read_products():
        with open(os.path.join(root_path, 'catalog.json'), 'r', encoding='utf-8') as r_file:
            raw_json = r_file.read()
            obj = json.loads(raw_json)
            new_obj = list(filter(lambda x: x['model'] == 'catalog.product', obj))
        return new_obj

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category["pk"], name=category["fields"]["name"],
                         description=category["fields"]["description"]))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product["pk"], name=product["fields"]["name"], description=product["fields"]["description"],
                        category_id=product["fields"]["category"], price=product["fields"]["price"]))

        Product.objects.bulk_create(product_for_create)
