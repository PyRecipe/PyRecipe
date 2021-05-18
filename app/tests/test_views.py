from django.test import TestCase, Client
from django.urls import reverse
from app.models import Recipe

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.recipe1 = Recipe.objects.create(
            slug = "recipe",
            title = "Recipe",
            author = 1
        )
        self.recipe_url = reverse('app:recipe', args=['recipe'])
        self.recipe_undefined_url = reverse('app:recipe', args=['this-recipe-not-exists'])
        self.search_url = reverse('app:search')

    def test_recipe_GET(self):
        response = self.client.get(self.recipe_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe.html')

    def test_recipe_GET_recipe_not_found(self):
        response = self.client.get(self.recipe_undefined_url)

        # is it redirected
        self.assertEquals(response.status_code, 302)

    def test_search_POST(self):
        response = self.client.post(
          self.search_url,
          {
              'search': "recipe",
          }
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search-list.html')

    def test_search_POST_empty_search(self):
        response = self.client.post(
          self.search_url,
          {
              'search': "",
          }
        )

        # redirects to homepage
        self.assertEquals(response.status_code, 302)
