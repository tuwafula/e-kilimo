import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
	'''
	creating a manager for a custom user model

    '''
	def create_user(self, email, password=None):
		"""
		Create and return a `User` with an email, username and password.
		"""
		if not email:
			raise ValueError('Users Must Have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Create and return a `User` with superuser (admin) permissions.
		"""
		if password is None:
			raise TypeError('Superusers must have a password.')      
		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user
      

	def create_farmeruser(self,email,password):
		if password is None:
			raise TypeError('Farmer must have a password')
		user = self.create_user(email,password)
		user.is_farmer = True
		user.save()
		return user


	def create_inputuser(self,email,password):
		if password is None:
			raise TypeError('Input holder must have a password')
		user = self.create_user(email,password)
		user.is_input_holder = True
		user.save()
		return user

    
	def create_investoruser(self,email,password):
		if password is None:
			raise TypeError('Investor must have a password')
		user = self.create_user(email,password)
		user.is_investor = True
		user.save()
		return user


	def create_tenderuser(self,email,password):
		if password is None:
			raise TypeError('Tender holder must have a password')
		user = self.create_user(email,password)
		user.is_tender_holder = True
		user.save()
		return user

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True
	)
    username = models.CharField(max_length=40, unique=False, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=False)
    is_tender_holder = models.BooleanField(default=False)
    is_investor = models.BooleanField(default=False)
    is_input_holder = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

	# Tells Django that the UserManager class defined above should manage
	# objects of this type.
    objects = UserManager()

    def __str__(self):
	    return self.email

class Meta:
	'''
	to set table name in database
	'''
	db_table = "login"


