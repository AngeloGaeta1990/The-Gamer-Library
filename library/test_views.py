from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Platform, Game, WishListGame
from .forms import EditPlatformForm, EditGameForm, EditWishListGameForm


class TestLibraryViews(TestCase):
    """
    Test class for the views of the library app.
    """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.login()
        self.platform = Platform(name="Test PC", user=self.user,
                                 slug="test-pc", category="PC")
        self.platform.save()

        self.game = Game(name="Test Game", platform=self.platform,
                         slug="test-game", user_score="70")
        self.game.save()

        self.wishlist_game = WishListGame(name="Wanted Game",
                                          platform=self.platform, priority="1")
        self.wishlist_game.save()

    def login(self):
        """
        Method to login the user.
        """
        self.client.login(username="myUsername", password="myPassword")

    def test_render_platform_detail_page(self):
        """
        Test for rendering the platform detail page.
        """
        response = self.client.get(reverse(
            'platform_detail', args=[self.user.id, self.platform.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test PC", response.content)
        self.assertIn(b"PC", response.content)

    def test_add_platform(self):
        """
        Test for posting a platform on a post
        """
        platform_data = {
            "name": "Test PC",
            "user": self.user.id,
            "slug": "test-pc",
            "category": "PC"
        }
        response = self.client.post(reverse(
            'platform_detail', args=[self.user.id, self.platform.id]),
                                    platform_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Test PC',
            response.content
        )

    def test_platform_list_view(self):
        """
        Test for rendering the platform list view.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/index.html')
        self.assertQuerysetEqual(response.context['platforms'],
                                 Platform.objects.filter(user=self.user),
                                 transform=lambda x: x)

    def test_edit_platform_view(self):
        """
        Test for rendering the edit platform view.
        """
        response = self.client.get(reverse('edit_platform',
                                           args=[self.user.id,
                                                 self.platform.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/edit_platform_form.html')
        self.assertIsInstance(response.context['edit_platform_form'],
                              EditPlatformForm)
        updated_data = {
            'name': 'Updated PC',
            'category': 'pc'
        }
        response = self.client.post(reverse('edit_platform',
                                            args=[self.user.id,
                                                  self.platform.id]),
                                    updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.platform.refresh_from_db()
        self.assertEqual(self.platform.name, 'Updated PC')

    def test_delete_platform_view(self):
        """
        Test for deleting a platform.
        """
        response = self.client.post(reverse('delete_platform',
                                            args=[self.user.id,
                                                  self.platform.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(Platform.objects.filter(pk=self.platform.pk).exists())

    def test_render_game_detail_page(self):
        """
        Test for rendering the game detail page.
        """
        response = self.client.get(reverse(
            'game_detail', args=[self.user.id, self.platform.id,
                                 self.game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Game")
        self.assertContains(response, "70")

    def test_add_game(self):
        """
        Test for adding a game.
        """
        game_data = {
            "name": "New Game",
            "platform": self.platform.id,
            "slug": "new-game",
            "user_score": "90",
        }
        response = self.client.post(reverse('add_game'), game_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Game.objects.filter(name="New Game").exists())

    def test_edit_game_view(self):
        """
        Test for rendering the edit game view.
        """
        response = self.client.get(reverse('edit_game', args=[self.user.id,
                                                              self.platform.id,
                                                              self.game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/edit_game_form.html')
        self.assertIsInstance(response.context['edit_game_form'], EditGameForm)
        updated_data = {
            'name': 'Updated Game',
            'platform': self.platform.id,
            'user_score': '70',
        }
        response = self.client.post(reverse('edit_game', args=[self.user.id,
                                            self.platform.id, self.game.id]),
                                    updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('game_detail', args=[
            self.user.id, self.platform.id, self.game.id]))
        self.game.refresh_from_db()
        self.assertEqual(self.game.name, 'Updated Game')

    def test_render_wishlist_game_detail_page(self):
        """
        Test for rendering the wishlist game detail page.
        """
        response = self.client.get(reverse('wishlist_game_detail',
                                           args=[self.user.id,
                                                 self.platform.id,
                                                 self.wishlist_game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Wanted Game")
        self.assertContains(response, "1")

    def test_add_wishlist_game(self):
        """
        Test for adding a game to the wishlist.
        """
        wishlist_game_data = {
            "name": "New Wishlist Game",
            "platform": self.platform.id,
            "priority": "3",
        }
        response = self.client.post(reverse('add_wishlist'),
                                    wishlist_game_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(WishListGame.objects.filter(
            name="New Wishlist Game").exists())

    def test_edit_wishlist_game_view(self):
        """
        Test for rendering the edit wishlist game view.
        """
        response = self.client.get(reverse('edit_wishlist_game',
                                           args=[self.user.id,
                                                 self.platform.id,
                                                 self.wishlist_game.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/'
                                'edit_wishlist_game_form.html')
        self.assertIsInstance(response.context['edit_wishlist_game_form'],
                              EditWishListGameForm)
        updated_data = {
            'name': 'Updated Wishlist Game',
            'platform': self.platform.id,
            'priority': '5',
        }
        response = self.client.post(reverse('edit_wishlist_game',
                                            args=[self.user.id,
                                                  self.platform.id,
                                                  self.wishlist_game.id]),
                                    updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('wishlist_game_detail',
                                               args=[self.user.id,
                                                     self.platform.id,
                                                     self.wishlist_game.id]))
        self.wishlist_game.refresh_from_db()
        self.assertEqual(self.wishlist_game.name, 'Updated Wishlist Game')

    def test_delete_wishlist_game_view(self):
        """
        Test for deleting a game from the wishlist.
        """
        response = self.client.post(reverse('delete_wishlist_game',
                                            args=[self.user.id,
                                                  self.platform.id,
                                                  self.wishlist_game.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(WishListGame.objects.filter(
            pk=self.wishlist_game.pk).exists())
