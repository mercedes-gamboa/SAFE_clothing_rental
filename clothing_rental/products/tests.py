from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.core.files.uploadedfile import SimpleUploadedFile

from products.views import AddClothingView, ClothingItemDetailView, ClothingItemListView, ClothesListView, add_clothes, \
    CategoryCreateView, CategoryListView, VariationCreateView, VariationListView, VariationOptionsCreateView, \
    VariationOptionListView, ClothingConfigurationCreateView, ClothingConfigurationListView, InventoryCreateView, \
    InventoryListView, CartListView, FavouritesListView, ClothingItemDeleteView, ClothingItemUpdateView, \
    ClothesDeleteView, ClothesUpdateView, ClothesDetailView, CategoryDeleteView, CategoryDetailView, CategoryUpdateView, \
    VariationOptionDeleteView, VariationOptionDetailView, VariationOptionUpdateView, ClothingConfigurationDeleteView, \
    ClothingConfigurationDetailView, ClothingConfigurationUpdateView, InventoryDeleteView, InventoryDetailView, \
    InventoryUpdateView, AddToFavouritesView, RemoveFavoriteView, AddToCartView

from products.models import Category, Clothes, ClothingItem
from accounts.models import ShoppingCart

User = get_user_model()
class TestUrls(SimpleTestCase):

    def test_new_clothing_item_url(self):
        url = reverse('new_clothing_item')
        # print(resolve(url))

        view = resolve(url).func.view_class
        # assert view == AddClothingView
        self.assertEqual(view, AddClothingView)


    def test_clothing_item_variaty_url(self):
        url = reverse('clothing_item_variaty')

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothingItemListView)


    def test_clothes_list_url(self):
        url = reverse('clothes_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothesListView)

    def test_add_clothes_url(self):
        url = reverse('new_clothes')

        view = resolve(url).func
        self.assertEqual(view, add_clothes)

    def test_add_category_url(self):
        url = reverse('add_category')

        view = resolve(url).func.view_class
        self.assertEqual(view, CategoryCreateView)

    def test_add_variation_url(self):
        url = reverse('add_variation')

        view = resolve(url).func.view_class
        self.assertEqual(view, VariationCreateView)

    def test_variation_list_url(self):
        url = reverse('variation_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, VariationListView)

    def test_category_list_url(self):
        url = reverse('category_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, CategoryListView)

    def test_add_variationoption_url(self):
        url = reverse('add_variationoption')

        view = resolve(url).func.view_class
        self.assertEqual(view, VariationOptionsCreateView)

    def test_list_variationoption_url(self):
        url = reverse('variationoption_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, VariationOptionListView)

    def test_add_clothing_configuration_url(self):
        url = reverse('add_clothing_configuration')

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothingConfigurationCreateView)

    def test_clothing_configuration_list_url(self):
        url = reverse('clothing_configuration_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothingConfigurationListView)

    def test_add_item_to_inventory_url(self):
        url = reverse('add_item_inventory')

        view = resolve(url).func.view_class
        self.assertEqual(view, InventoryCreateView)

    def test_inventory_list_url(self):
        url = reverse('inventory_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, InventoryListView)

    def test_cart_list_url(self):
        url = reverse('cart_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, CartListView)

    def test_favourite_list_url(self):
        url = reverse('favourites_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, FavouritesListView)

    def test_detail_clothing_item_url(self):
        # url = reverse("clothing_item", args=[0])
        url = reverse("clothing_item", kwargs={'pk': 0})

        view = resolve(url).func.view_class
        # assert view == AddClothingView
        self.assertEqual(view, ClothingItemDetailView)

    def test_delete_clothing_item_url(self):
        url = reverse("delete_clothing_item", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothingItemDeleteView)

    def test_update_clothing_item_url(self):
        url = reverse("update_clothing_item", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothingItemUpdateView)

    def test_delete_clothes_type_url(self):
        url = reverse("delete_clothe", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothesDeleteView)

    def test_update_clothes_type_url(self):
        url = reverse("clothes_update", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothesUpdateView)

    def test_detail_clothes_type_url(self):
        url = reverse("detail_clothes", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothesDetailView)

    def test_delete_category_url(self):
        url = reverse("delete_category", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, CategoryDeleteView)

    def test_detail_category_url(self):
        url = reverse("category_detail", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, CategoryDetailView)

    def test_update_category_url(self):
        url = reverse("category_update", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, CategoryUpdateView)

    def test_delete_variationoption_url(self):
        url = reverse("delete_variationoption", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, VariationOptionDeleteView)

    def test_detail_variationoption_url(self):
        url = reverse("detail_variationoption", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, VariationOptionDetailView)

    def test_update_variationoption_url(self):
        url = reverse("update_variationoption", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, VariationOptionUpdateView)

    def test_delete_clothing_configuration_url(self):
        url = reverse("delete_clothing_configuration", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothingConfigurationDeleteView)

    def test_detail_clothing_configuration_url(self):
        url = reverse("detail_clothing_configuration", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothingConfigurationDetailView)

    def test_update_clothing_configuration_url(self):
        url = reverse("update_clothing_configuration", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, ClothingConfigurationUpdateView)

    def test_delete_inventory_item_url(self):
        url = reverse("delete_inventory_item", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, InventoryDeleteView)

    def test_detail_inventory_item_url(self):
        url = reverse("detail_inventory_item", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, InventoryDetailView)

    def test_update_inventory_item_url(self):
        url = reverse("update_inventory_item", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, InventoryUpdateView)

    def test_add_item_to_cart_url(self):
        url = reverse("add_to_cart", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, AddToCartView)

    def test_add_item_to_favourites_url(self):
        url = reverse("add_to_favourites", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, AddToFavouritesView)
    def test_remove_from_favourite_url(self):
        url = reverse("remove_favourite", args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, RemoveFavoriteView)

class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(email="test@test.test", password="XYY")

    def setUp(self):
        self.category_1 = Category.objects.create(category_name="pants")
        self.clothes_1 = Clothes.objects.create(
            category=self.category_1,
            clothing_name="capripants",
            description="xyq",
            clothing_image=SimpleUploadedFile(
                name='test.png',
                content=b'',
                content_type='image/png'
            )
        )
        self.clothing_item_1 = ClothingItem.objects.create(
            quantity_in_stock=3,
            item_image=SimpleUploadedFile(
                name='test2.png',
                content=b'',
                content_type='image/png'
            ),
            price = 10.00,
            clothes=self.clothes_1,
            code="ABC123",
            name="Tropical Blouse"
        )
        self.user.shoppingcart.clothing_items.set([self.clothing_item_1])


    def test_clothes_list_GET(self):
        self.client.force_login(self.user)
        url = reverse('clothes_list')
        response = self.client.get(url)
        # print(dir(response))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clothes_list.html')

        clothes_item = response.context["clothes"][0]
        self.assertIsInstance(clothes_item, Clothes)
        self.assertEqual(response.context["clothes"].count(), 1)
        self.assertEqual(clothes_item.clothing_name, self.clothes_1.clothing_name)
        # print(response.context["clothes"])


    def test_cart_list_view_GET(self):
        self.client.force_login(self.user)
        url = reverse('cart_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"products/cart_list.html")

        print(response.context)
        cart = response.context["shopping_cart"]
        self.assertIsInstance(cart, ShoppingCart)
        self.assertEqual(cart.user, self.user)
        self.assertEqual(cart.clothing_items.count(), 1)
        self.assertEqual(cart.clothing_items.first(), self.clothing_item_1)
