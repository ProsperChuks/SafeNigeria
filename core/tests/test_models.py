from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model


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
