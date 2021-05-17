from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Recipe, Comment


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.recipe1 = Recipe.objects.create(
            slug = "recipe",
            title = "Recipe",
            description= "Recipe Descriptions",
            author = 1
        )
        self.recipe_url = reverse('app:recipe', args=['recipe'])
        self.recipe_undefined_url = reverse('app:recipe', args=['this-recipe-not-exists'])


        #  register setUp
        self.register_url = reverse('app:register')


        self.my_recipes_url = reverse('app:my_recipes')




    """ Recipe View Tests """

    def test_recipe_GET(self):
        response = self.client.get(self.recipe_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe.html')

    def test_recipe_GET_recipe_not_found(self):
        response = self.client.get(self.recipe_undefined_url)

        # is it redirected
        self.assertEquals(response.status_code, 302)



    """ Register Tests  """
    
    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_create_user(self):
        amount_of_user = len(User.objects.all())
        response = self.client.post(
            self.register_url,
            {
                'first_name': 'Kevin',
                'last_name' : 'Wmes',
                'username' : 'example12321',
                'email': 'example34@hotmail.com',
                'password1' : 'Aa90019001',
                'password2' : 'Aa90019001'
            }
        ) 
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(User.objects.all()),amount_of_user + 1)
        




    """ Comment Tests """
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






        


    """ My Recipes View Tests"""
    def test_my_recipes_GET(self):
        response = self.client.get(self.my_recipes_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_recipes.html') 

