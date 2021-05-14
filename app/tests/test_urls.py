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
        self.assertEquals(resolve(url).func, views.login)

    def test_signup_url_is_resolved(self):
        url = reverse('app:signup')
        self.assertEquals(resolve(url).func, views.signup)

    def test_search_url_is_resolved(self):
        url = reverse('app:searching')
        self.assertEquals(resolve(url).func, views.searching)

    def test_search_listing_url_is_resolved(self):
        url = reverse('app:search-listing')
        self.assertEquals(resolve(url).func, views.searchListing)

    def test_edit_url_is_resolved(self):
        url = reverse('app:editing')
        self.assertEquals(resolve(url).func, views.editing)

    def test_add_url_is_resolved(self):
        url = reverse('app:adding')
        self.assertEquals(resolve(url).func, views.adding)

    def test_my_recipes_url_is_resolved(self):
        url = reverse('app:my_recipes')
        self.assertEquals(resolve(url).func, views.my_recipes)

    def test_recipe_url_is_resolved(self):
        url = reverse('app:recipe', args=['recipe'])
        self.assertEquals(resolve(url).func, views.recipe)
