from django.test import SimpleTestCase
from django.urls import reverse, resolve

import app.views as views

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        # reverse() requires => namespace:view_name
        # this project using namespace as app
        url = reverse('app:index')
        self.assertEquals(resolve(url).func, views.index)

    def test_settings_url_is_resolved(self):
        url = reverse('app:settings')
        self.assertEquals(resolve(url).func, views.settings)

    def test_login_url_is_resolved(self):
        url = reverse('app:login')
        self.assertEquals(resolve(url).func, views.userLogin)

    def test_register_url_is_resolved(self):
        url = reverse('app:register')
        self.assertEquals(resolve(url).func, views.register)

    def test_search_url_is_resolved(self):
        url = reverse('app:search')
        self.assertEquals(resolve(url).func, views.search)

    def test_search_list_url_is_resolved(self):
        url = reverse('app:search-list')
        self.assertEquals(resolve(url).func, views.searchList)

    def test_edit_url_is_resolved(self):
        url = reverse('app:edit')
        self.assertEquals(resolve(url).func, views.edit)

    def test_add_url_is_resolved(self):
        url = reverse('app:add')
        self.assertEquals(resolve(url).func, views.add)

    def test_my_recipes_url_is_resolved(self):
        url = reverse('app:my_recipes')
        self.assertEquals(resolve(url).func.view_class, views.MyRecipes)

    def test_recipe_url_is_resolved(self):
        url = reverse('app:recipe', args=['recipe'])
        self.assertEquals(resolve(url).func, views.recipe)
