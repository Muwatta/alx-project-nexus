# catalog/management/commands/populate_sample_data.py
from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from faker import Faker
import random

class Command(BaseCommand):
    help = "Populate sample categories and products"

    def handle(self, *args, **options):
        fake = Faker()

        # Sample categories
        categories = [
            {"name": "Electronics", "description": "Electronic devices"},
            {"name": "Books", "description": "Books and literature"},
            {"name": "Clothing", "description": "Men and Women clothing"},
            {"name": "Home & Kitchen", "description": "Home and kitchen products"},
            {"name": "Toys & Games", "description": "Toys for kids and adults"},
        ]

        # Create categories
        for cat_data in categories:
            cat, created = Category.objects.get_or_create(**cat_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Category created: {cat.name}"))

        # Create 20 random products
        category_objects = list(Category.objects.all())
        for _ in range(20):
            cat = random.choice(category_objects)
            product_data = {
                "name": fake.unique.word().title(),
                "description": fake.sentence(nb_words=10),
                "price": round(random.uniform(5.0, 999.99), 2),
                "stock": random.randint(10, 500),
                "category": cat,
            }
            prod, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Product created: {prod.name} ({cat.name})"))
