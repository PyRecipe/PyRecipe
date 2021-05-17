from django.test import TestCase, Client
from django.urls import reverse
from app.models import Recipe, Comment

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

    def test_recipe_GET(self):
        response = self.client.get(self.recipe_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe.html')

    def test_recipe_GET_recipe_not_found(self):
        response = self.client.get(self.recipe_undefined_url)

        # is it redirected
        self.assertEquals(response.status_code, 302)

    def test_create_comment(self):
        comment_count = len(Comment.objects.all())
        response = self.client.post(
          self.recipe_url,
          {
              'recipe_id': 1,
              'comment': "afamsdöfnams dnföasmfnödasf"
          }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Comment.objects.all()), comment_count + 1)

    def test_create_comment_without_comment(self):
        comment_count = len(Comment.objects.all())

        response = self.client.post(
          self.recipe_url,
          {
              'recipe_id': 1,
              'comment': ""
          }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Comment.objects.all()), comment_count)