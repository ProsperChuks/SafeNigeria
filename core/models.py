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
		user.superuser = True
		user.save()
		return user



class CustomUser(AbstractUser):
	email = models.EmailField(max_length=100, unique=True)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	avatar = models.ImageField(
        upload_to='profilepics', 
        blank=True, 
        null=True
    )
	is_active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) 
	superuser = models.BooleanField(default=False)
	objects = UserManager( )

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email',]

	def __str__( self ):
		return self.get_full_name()
	
	def get_full_name(self):
		return f"{self.first_name} {self.last_name}".title()
	
	def is_staff(self):
		return self.is_staff
	
	def is_superuser(self):
		return self.superuser




# List of all cities in Nigeria
CITIES = (
	('abia', 		'Abia'),
	('adamawa', 	'Adamawa',),
	('akwaibom', 	'Akwa Ibom'),
	('anambra', 	'Anambra',),
	('bauchi', 		'Bauchi'),
	('bayelsa', 	'Bayelsa'),
	('benue', 		'Benue'),
	('Borno', 		'Borno'),
	('crossriver', 	'Cross River'),
	('delta', 		'Delta'),
	('ebonyi', 		'Ebonyi'),
	('enugu', 		'Enugu'),
	('edo', 		'Edo'),
	('ekiti', 		'Ekiti'),
	('gombe', 		'Gombe'),
	('imo', 		'Imo'),
	('jigawa', 		'Jigawa'),
	('kaduna', 		'Kaduna'),
	('kano', 		'Kano'),
	('katsina', 	'Katsina'),
	('kebbi', 		'Kebbi'),
	('kogi', 		'Kogi'),
	('kwara', 		'Kwara'),
	('lagos', 		'Lagos'),
	('nasarawa', 	'Nasarawa'),
	('niger', 		'Niger'),
	('ogun', 		'Ogun'),
	('ondo', 		'Ondo'),
	('osun', 		'Osun'),
	('oyo', 		'Oyo'),
	('plateau', 	'Plateau'),
	('rivers', 		'Rivers'),
	('sokoto', 		'Sokoto'),
	('taraba', 		'Taraba'),
	('yobe', 		'Yobe'),
	('zamfara', 	'Zamfara')
)




class State(models.Model):
	name = models.CharField(max_length=18, choices=CITIES)

	def __str__(self):
		return self.name.title()



class Incident(models.Model):
	description = models.TextField()
	video = models.FileField(upload_to='uploaded_videos')
	headline = models.CharField(max_length=225, blank=False, null=False)
	date_uploaded = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(
		get_user_model(), 
		on_delete=models.CASCADE, 
		related_name='incidents'
	)
	city = models.ForeignKey(
		State,
		related_name='incidents',
		on_delete=models.CASCADE
	)

	class Meta:
		ordering = ['-date_uploaded']

	def __str__(self):
		return self.headline.title()
	
	def save(self, *args, **kwargs):
		self.headline = self.headline.title()
		super(Incident, self).save(*args, **kwargs)

