from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Recipe, Comment

class TestViews(TestCase):
    def setUp(self):
        """Test setUp"""
        self.client = Client()
        self.recipe1 = Recipe.objects.create(
            slug = "recipe",
            title = "Recipe",
            description= "Recipe Descriptions",
            author = 1
        )
        self.user1_credentials = {
            'first_name' : 'Deneme',
            'last_name' : 'denemesoyad',
            'username' : 'denemeusername',
            'email' : 'denememail@hotmail.com',
            'password' : 'Aa9001900a1'
        }

        User.objects.create_user(**self.user1_credentials)
        
        self.recipe_url = reverse('app:recipe', args=['recipe'])
        self.recipe_undefined_url = reverse('app:recipe', args=['this-recipe-not-exists'])
        self.search_url = reverse('app:search')
        self.register_url = reverse('app:register')
        self.my_recipes_url = reverse('app:my_recipes')
        self.settings_url = reverse('app:settings')
        self.login_url = reverse('app:login')
        self.delete_recipe_url = reverse('app:recipe_delete',args=['recipe2'])

    """ Recipe View Tests """
    def test_recipe_GET(self):
        response = self.client.get(self.recipe_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe.html')

    def test_recipe_GET_recipe_not_found(self):
        response = self.client.get(self.recipe_undefined_url)

        # redirect to homepage
        self.assertEquals(response.status_code, 302)
        
    """ Recipe Search Tests """
    def test_search_POST(self):
        response = self.client.post(
          self.search_url,
          {
              'search': "recipe",
          }
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search-list.html')
        
    def test_search_POST_empth_search(self):
        response = self.client.post(
          self.search_url,
          {
            'search': "",
          }
        )
        
        # redirect to homepage
        self.assertEquals(response.status_code, 302)
  
    """ Register Tests """
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
        
        self.assertEqual(response.status_code, 302)
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


    """ Settings Tests """
    def test_settings_GET(self):
        response = self.client.get(self.settings_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings.html')

    def test_settings_POST(self):
        self.test_login_user_POST() # because of login is required
        response = self.client.post(
            self.settings_url,
            {
                'first_name': "ayarlar321",
                'last_name' : "ayarlarsoyad",
                'email' : 'ayarlar@hotmail.com'
            }
        )
        
        self.assertEquals(response.status_code, 302)
        
    
    """ Login View Tests """
    def test_login_GET(self):
        response = self.client.get(self.login_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html') 

    def test_login_user_POST(self):
        response = self.client.post(
            self.login_url,
            {
                'username' : "denemeusername",
                'password' : "Aa9001900a1"
            }
        ) 

        self.assertEquals(response.status_code, 302)

    """ Recipe deleting test """
    def test_recipe_deleting(self):

        self.test_login_user_POST()
        recipe = Recipe.objects.create(
            slug = "recipe2",
            title = "Ornek",
            description= "Recipe Description",
            author = 2
        )

        recipe_count = len(Recipe.objects.all())
        response = self.client.get(self.delete_recipe_url)
    
        self.assertEquals(recipe_count, len(Recipe.objects.all()) + 1)