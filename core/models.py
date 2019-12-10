from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager( BaseUserManager ):
	def create_user(self, username, email, password = None):
		"""
		Creates and saves a User with the given mobile_number and password
		"""
		if not email:
			raise ValueError( 'email address required' )
		if not username:
			raise ValueError( 'username required' )
		
		
		user = self.model(
			username=username,
			email = self.normalize_email(email),
		)

		user.set_password(password)
		user.save( )
		return user


	def create_staffuser(self, username, email, password):
		"""
		Creates and saves a staff user with the given email and password
		"""
		user = self.create_user( 
			username=username, 
			email=email, 
			password=password 
		)
		user.staff = True
		user.save( )
		return user


	def create_superuser(self, username, email, password):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user( 
			username=username, 
			email=email, 
			password=password 
		)
		user.staff = True
		user.admin = True
		user.save()
		return user



class CustomUser(AbstractUser):
	email = models.EmailField(max_length=100,)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	avatar = models.ImageField(
        upload_to='profilepics', 
        blank=True, 
        null=True
    )
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) 
	admin = models.BooleanField(default=False)
	objects = UserManager( )

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email',]

	def __str__( self ):
		return self.email
	
	def get_full_name(self):
		return f"{self.first_name.title()} {self.last_name.title()}"

