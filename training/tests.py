from django.test import TestCase, Client
from django.urls import reverse
from training.models import Trainer, Athlete
from training.forms import AthleteForm
from datetime import date


class ModelTests(TestCase):
    def setUp(self):
        self.trainer = Trainer.objects.create_user(
            username="testtrainer",
            password="testpass123",
            first_name="John",
            last_name="Doe",
            specialization="Strength Training",
            years_experience=5
        )

        self.athlete = Athlete.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com",
            date_of_birth=date(1995, 5, 15),
            trainer=self.trainer
        )

    def test_trainer_str_method(self):
        """Test trainer string representation"""
        self.assertEqual(
            str(self.trainer),
            "testtrainer (Strength Training)"
        )

    def test_athlete_str_method(self):
        """Test athlete string representation"""
        self.assertEqual(str(self.athlete), "Jane Smith")

    def test_athlete_trainer_relationship(self):
        """Test athlete is linked to trainer"""
        self.assertEqual(self.athlete.trainer, self.trainer)
        self.assertIn(self.athlete, self.trainer.athletes.all())


class FormTests(TestCase):
    def setUp(self):
        self.trainer = Trainer.objects.create_user(
            username="trainer1",
            password="pass123",
            specialization="Cardio",
            years_experience=3
        )

        self.athlete = Athlete.objects.create(
            first_name="Test",
            last_name="Athlete",
            email="test@test.com",
            date_of_birth=date(2000, 1, 1),
            trainer=self.trainer
        )

    def test_athlete_form_valid(self):
        """Test athlete form with valid data"""
        form_data = {
            "first_name": "New",
            "last_name": "Athlete",
            "email": "new@test.com",
            "date_of_birth": "2000-01-01",
            "trainer": self.trainer.id
        }
        form = AthleteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_athlete_form_invalid_email(self):
        """Test athlete form with duplicate email"""
        form_data = {
            "first_name": "Another",
            "last_name": "Athlete",
            "email": "test@test.com",
            "date_of_birth": "2000-01-01",
            "trainer": self.trainer.id
        }
        form = AthleteForm(data=form_data)
        self.assertFalse(form.is_valid())


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.trainer = Trainer.objects.create_user(
            username="testuser",
            password="testpass123",
            specialization="CrossFit",
            years_experience=2
        )

        self.athlete = Athlete.objects.create(
            first_name="Test",
            last_name="User",
            email="testuser@test.com",
            date_of_birth=date(1990, 1, 1),
            trainer=self.trainer
        )

    def test_index_requires_login(self):
        """Test index page requires login"""
        response = self.client.get(reverse("training:index"))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_index_works_when_logged_in(self):
        """Test index page works when logged in"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("training:index"))
        self.assertEqual(response.status_code, 200)

    def test_athlete_list_requires_login(self):
        """Test athlete list requires login"""
        response = self.client.get(reverse("training:athlete-list"))
        self.assertEqual(response.status_code, 302)

    def test_athlete_list_works_when_logged_in(self):
        """Test athlete list works when logged in"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("training:athlete-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")

    def test_athlete_detail_shows_correct_info(self):
        """Test athlete detail page shows correct information"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(
            reverse("training:athlete-detail", kwargs={"pk": self.athlete.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")
        self.assertContains(response, "testuser@test.com")

    def test_athlete_create_view(self):
        """Test creating new athlete"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("training:athlete-create"),
            {
                "first_name": "New",
                "last_name": "Athlete",
                "email": "new@athlete.com",
                "date_of_birth": "1995-06-15",
                "trainer": self.trainer.pk
            }
        )
        self.assertEqual(Athlete.objects.count(), 2)
        self.assertTrue(
            Athlete.objects.filter(email="new@athlete.com").exists()
        )

    def test_login_view(self):
        """Test login functionality"""
        response = self.client.post(
            reverse("training:login"),
            {"username": "testuser", "password": "testpass123"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("training:index"))


class SearchTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.trainer = Trainer.objects.create_user(
            username="searchuser",
            password="pass123",
            specialization="Yoga",
            years_experience=1
        )

        self.athlete1 = Athlete.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@test.com",
            date_of_birth=date(1990, 1, 1),
            trainer=self.trainer
        )

        self.athlete2 = Athlete.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane@test.com",
            date_of_birth=date(1992, 2, 2),
            trainer=self.trainer
        )

        self.client.login(username="searchuser", password="pass123")

    def test_athlete_search_by_name(self):
        """Test searching athletes by name"""
        response = self.client.get(
            reverse("training:athlete-list"),
            {"name": "John"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertNotContains(response, "Jane Smith")

    def test_athlete_search_case_insensitive(self):
        """Test search is case insensitive"""
        response = self.client.get(
            reverse("training:athlete-list"),
            {"name": "JOHN"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
