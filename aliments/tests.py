from django.test import TestCase
from aliments.models import Category
from aliments.models import Store
from aliments.models import Products
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegistrationForm


# models test
class CategoryTest(TestCase):

    def create_Category(self, nameCategory='Cat1', idCategory='idCat1'):
        return Category.objects.create(nameCategory=nameCategory,
                                       idCategory=idCategory)

    def create_Store(self, nameStore='Sto1', idStore='idSto1'):
        return Store.objects.create(nameStore=nameStore, idStore=idStore)

    def create_Products(self):
        c = self.create_Category()
        s = self.create_Store()
        self.assertTrue(isinstance(c, Category))
        self.assertTrue(isinstance(s, Store))

        nameAlim = "Gazpacho"
        image = "https://static.openfoodfacts.org/images/products/541/018/" \
                "803/1072/front_fr.30.200.jpg"
        url = "https://world.openfoodfacts.org/product/5410188031072/"\
              "gazpacho-alvalle"
        descriptionAlim = "Tomate, poivron, concombre, oignon, huile d'olive"\
                          "extra vierge, eau, vinaigre de vin, sel, ail"\
                          "et jus de citron."
        nutritionGrade = "a"
        idCategory = (c)
        idStore = (s)
        return Products.objects.create(nameAlim=nameAlim,
                                       image=image, url=url,
                                       descriptionAlim=descriptionAlim,
                                       nutritionGrade=nutritionGrade,
                                       idCategory=idCategory,
                                       idStore=idStore)

    def test_Category_creation(self):
        c = self.create_Category()
        s = self.create_Store()
        p = self.create_Products()

        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), c.nameCategory)
        self.assertTrue(isinstance(s, Store))
        self.assertEqual(s.__str__(), s.nameStore)
        self.assertTrue(isinstance(p, Products))
        self.assertEqual(p.__str__(), p.nameAlim)

    def test_text_content(self):
        p = self.create_Products()
        expected_object_name = f'{p.nameAlim}'
        self.assertEquals(expected_object_name, 'Gazpacho')

    """def test_post_list_view(self):
        p = self.create_Products()
        p.save()
        product = p.objects.get(pk=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(product.get_absolute_url(), '/results_details/1')"""


class CommentFormTest(TestCase):

    def test_valid_data(self):
        obj_user = RegistrationForm({"Joana Silva",
                                     "joana@example.com",
                                     "password1",
                                     "password2"})

        self.assertEqual(obj_user['username'], "Joana Silva")
        self.assertEqual(obj_user['email'], "joana@example.com")
