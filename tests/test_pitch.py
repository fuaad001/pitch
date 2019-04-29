import unittest
from app.models import Pitch,User,Review

class TestPitch(unittest.TestCase):
    """
    This is the class which we will use to do tests for the Pitch
    """

    def setUp(self):
        """
        This will create an instance of the User and Pitch before each test case
        """
        self.new_user = User(username = "Fuaad")
        self.new_pitch = Pitch(title = "pitch", user = self.new_user)

    def tearDown(self):
        """
        Will delete all the info from the db
        """
        Pitch.query.delete()
        User.query.delete()
        Review.query.delete()

    def test_instance(self):
        """
        Will test whether the new_pitch is an instance of Pitch
        """
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_init(self):
        """
        Will test whether the new_pitch is instantiated correctly
        """

        self.assertEquals(self.new_pitch.title, "pitch")

    def test_save_pitch(self):
        """
        Will test whether the user is saved into the database
        """
        self.new_pitch.save_pitch()
        pitches = Pitch.query.all()
        self.assertTrue(len(pitches) > 0)

    def test_relationship_user(self):
        """
        Will test whether the pitch is correctly related to the user who posted it
        """
        user = self.new_pitch.user.username
        self.assertTrue(user == "Fuaad")
