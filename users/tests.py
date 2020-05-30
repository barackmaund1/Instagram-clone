from django.test import TestCase
from .models import Profile
# Create your tests here.
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='barack')
        self.user.save()

        self.profile_test = Profile(id=1, image='default.jpg', bio='this is a test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)