from django.test import TestCase

from products.models import Category, Product, Tag


class TagModelTests(TestCase):
    def test_tag_string_representation_returns_name(self) -> None:
        tag = Tag.objects.create(name="New")

        self.assertEqual(str(tag), "New")

    def test_product_can_have_multiple_tags(self) -> None:
        category = Category.objects.create(
            name="Strollers",
            slug="strollers",
            description="Products for strollers",
        )
        product = Product.objects.create(
            category=category,
            name="Baby Stroller",
            description="Comfortable baby stroller",
            price="199.99",
        )
        first_tag = Tag.objects.create(name="Popular")
        second_tag = Tag.objects.create(name="Recommended")

        product.tags.add(first_tag, second_tag)

        self.assertEqual(product.tags.count(), 2)
        self.assertIn(first_tag, product.tags.all())
        self.assertIn(second_tag, product.tags.all())

    def test_product_tags_are_optional(self) -> None:
        category = Category.objects.create(
            name="Toys",
            slug="toys",
            description="Baby toys",
        )
        product = Product.objects.create(
            category=category,
            name="Baby Toy",
            description="Small baby toy",
            price="19.99",
        )

        self.assertEqual(product.tags.count(), 0)
