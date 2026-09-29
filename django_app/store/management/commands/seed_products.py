from django.core.management.base import BaseCommand
from store.models import Product


class Command(BaseCommand):
    help = "Add demo products"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()

        products = [
            {
                "name": "boAt Airdopes 141",
                "category": "Electronics",
                "description": "Wireless earbuds with long battery life and clear sound.",
                "price": 1299,
                "old_price": 4490,
                "rating": 4.2,
                "reviews": 18432,
                "stock": 25,
                "image": "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?w=600",
                "badge": "Limited Deal",
                "is_deal": True,
            },
            {
                "name": "Samsung Galaxy Smartphone",
                "category": "Mobiles",
                "description": "Modern smartphone with a bright display and powerful performance.",
                "price": 18999,
                "old_price": 22999,
                "rating": 4.4,
                "reviews": 8421,
                "stock": 15,
                "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600",
                "badge": "Deal of the Day",
                "is_deal": True,
            },
            {
                "name": "Wireless Mechanical Keyboard",
                "category": "Computers",
                "description": "Compact mechanical keyboard suitable for work and gaming.",
                "price": 2499,
                "old_price": 3999,
                "rating": 4.3,
                "reviews": 3210,
                "stock": 30,
                "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=600",
                "badge": "20% off",
                "is_deal": True,
            },
            {
                "name": "Men's Casual Sneakers",
                "category": "Fashion",
                "description": "Comfortable everyday sneakers with a clean casual design.",
                "price": 1599,
                "old_price": 2999,
                "rating": 4.1,
                "reviews": 5234,
                "stock": 40,
                "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600",
                "badge": "Best Seller",
                "is_deal": False,
            },
            {
                "name": "Modern Desk Lamp",
                "category": "Home",
                "description": "Minimal LED desk lamp for study and workspace setups.",
                "price": 899,
                "old_price": 1499,
                "rating": 4.5,
                "reviews": 2187,
                "stock": 20,
                "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=600",
                "badge": "Top Rated",
                "is_deal": False,
            },
            {
                "name": "Python Programming Book",
                "category": "Books",
                "description": "Beginner-friendly guide to learning Python programming.",
                "price": 599,
                "old_price": 899,
                "rating": 4.6,
                "reviews": 1456,
                "stock": 50,
                "image": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=600",
                "badge": "Popular",
                "is_deal": False,
            },
            {
                "name": "Face Care Essentials",
                "category": "Beauty",
                "description": "Simple daily skincare essentials for a fresh routine.",
                "price": 749,
                "old_price": 999,
                "rating": 4.0,
                "reviews": 982,
                "stock": 35,
                "image": "https://images.unsplash.com/photo-1556228578-8c89e6adf883?w=600",
                "badge": "New",
                "is_deal": False,
            },
        ]

        for product in products:
            Product.objects.create(**product)

        self.stdout.write(
            self.style.SUCCESS(
                f"Added {len(products)} demo products."
            )
        )
