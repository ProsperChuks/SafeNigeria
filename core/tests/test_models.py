import os

from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError, DataError

from core.models import State, Incident


class CustomUserTest(TestCase):
    """
    handles neccessary test required for CustomUser model
    """
    
    def setUp(self):
        self.john_user = get_user_model().objects.create(
            username = 'johndoe',
            email = 'johndoe@gmail.com',
        )
        self.john_user.set_password("johndoepass")


        self.jane_user = get_user_model().objects.create(
            username = 'janedoe',
            email = 'janedoe@gmail.com',
        )
        self.jane_user.set_password("janedoepass")

    
    def test_get_full_name_returns_right_value(self):
        """
        get_full_name is a helper method that returns the 
        first name and last name of a user as a single value.
        Test confirms that this method confirms appropriately.
        """
        # check for john user
        self.john_user.first_name = "John"
        self.john_user.last_name = "Doe"
        self.john_user.save()

        self.assertEqual(self.john_user.get_full_name(), "John Doe".title())

        self.jane_user.first_name = "Jane"
        self.jane_user.last_name = "Doe"
        self.jane_user.save()

        self.assertEqual(self.jane_user.get_full_name(), "Jane Doe".title())


    def test_user_account_create_with_valid_data(self):
        """
        when valid data are inputted to create an account, then
        the account should be created successfully with the valid data
        """
        # check for john user
        self.assertEqual(self.john_user.username, "johndoe")
        self.assertEqual(self.john_user.email, "johndoe@gmail.com")
        self.assertTrue(self.john_user.check_password("johndoepass"))

        # check for jane user
        self.assertEqual(self.jane_user.username, "janedoe")
        self.assertEqual(self.jane_user.email, "janedoe@gmail.com")
        self.assertTrue(self.jane_user.check_password("janedoepass"))

    
    def test_invalid_user_password_on_password_check(self):
        """
        when an invalid password is passed for a user, test should fail
        """
        # check for jane
        self.assertFalse(self.jane_user.check_password("janedoepassword"))
        # check for john
        self.assertFalse(self.john_user.check_password("johndoepassword"))


    def test_no_two_email_can_exist(self):
        """
        when an email already exists, that email cannot be used to create
        another user
        """
        with self.assertRaises(IntegrityError):
            get_user_model().objects.create(
                username = 'johngeek',
                email = 'johndoe@gmail.com',
            )

    
    def test_no_two_or_more_user_account_can_be_the_same(self):
        """
        no two user account can be the same
        """
        self.assertNotEqual(self.john_user, self.jane_user)




class StateTest(TestCase):
    """
    handles neccessary test required for State model
    """

    def setUp(self):
        self.state_one = State.objects.create(name='jos')
        self.state_two = State.objects.create(name='ogun')

    def test_state_creates_successfull_with_valid_data(self):
        """
        a state creates successfully when the data that are used in
        creation are valid
        """
        self.assertIsInstance(self.state_one, State)
        self.assertIsInstance(self.state_two, State)

    def test_conformity_of_state_str_method(self):
        """
        state string representation should return the name of state in
        title case
        """
        self.assertEqual(self.state_two.__str__(), 'ogun'.title())
        self.assertEqual(self.state_one.__str__(), 'jos'.title())
    

    def test_state_creation_fails_with_invalid_value_as_choice(self):
        """
        test should fail if state to be created is not amn
        """
        # invalid_state = State.objects.create(name='labalaba')
        # self.assertNotIsInstance(invalid_state, State)
        pass



class IncidentTest(TestCase):
    """
    handles neccessary test required for Incident model
    """

    def setUp(self):

        # create two user account
        self.user_one = get_user_model().objects.create (
            username = 'johndoe',
            email = 'johndoe@gmail.com',
        )
        self.user_one.set_password("johndoepass")


        self.user_two = get_user_model().objects.create(
            username = 'janedoe',
            email = 'janedoe@gmail.com',
        )
        self.user_two.set_password("janedoepass")

        # create states
        self.state_one = State.objects.create(
            name = 'edo'
        )

        self.state_two = State.objects.create(
            name='jos'
        )

        # create incidents
        # with open(
        #     file = os.path.join(
        #         settings.BASE_DIR, 
        #         "static/test_dir/edited_winningeleven.mp4"))as file:
            
        self.incident_one = Incident.objects.create(
            headline = "test for incident one",
            user = self.user_one,
        )
        self.incident_one.city.add(self.state_one)

        self.incident_two = Incident.objects.create(
            headline = "test for incident two",
            user = self.user_two,
        )
        self.incident_two.city.add(self.state_two)


    def test_incident_successfully_created(self):
        # incident one
        self.assertIsInstance(self.incident_one, Incident)
        self.assertEqual(self.incident_one.__str__(), "Test For Incident One")
        self.assertIsInstance(self.incident_one.user, get_user_model())
        self.assertEqual(self.incident_one.city.get(name='edo'), self.state_one)

        # incident two
        self.assertIsInstance(self.incident_two, Incident)
        self.assertEqual(self.incident_two.__str__(), "Test For Incident Two")
        self.assertIsInstance(self.incident_two.user, get_user_model())
        self.assertEqual(self.incident_two.city.get(name='jos'), self.state_two)

    
    def test_incident_created_by_one_user_cannot_be_another_users_upload(self):
        """
        every incident belongs to the user that uploaded the incident 
        """
        self.assertNotEqual(
            self.incident_one.user, self.user_two
        )

        self.assertNotEqual(
            self.incident_two.user, self.user_one
        )

    def test_no_two_incident_are_separate_and_different(self):
        """
        two different incident should be different
        """
        self.assertNotEqual(self.incident_one, self.incident_two)
