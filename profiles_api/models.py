from django.db import models
from django.contrib.auth.models import AbstractBaseUser  
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

# Here AbstractBaseUser, PermissionsMixin are used when we do to some changes in django bydefault user model.

""" Now we have to created a function to manipulate all thq queries , we have to define each function
explicity , because we are using email and pass field , Not Bydefault field of django """

class UserProfileManager(BaseUserManager):
    """Manager profiles to handle the users accordingly"""

    def create_user(self,email,name,password=None):
        """Create A new User for the User Profile Model"""
        if not email:  ## checking if none or not provided email address for creating user profile
            raise ValueError('User Must Have Email Address')

        email= self.normalize_email(email) ## convert the whole email address to lowercase alphabets

        """Now Creating the user model """
        user=self.model(email=email,name=name) # SET EMAIL AND NAME , We can also pass password here but then 
        # the password is store in a clear text value, and if our system is hacked all the information steal
        # we are using set password function which encripted the password.

        user.set_password(password) # hashed or encripted password
        user.save(using=self._db)

        return user 

    def create_superuser(self,email,name,password):
        """Create and Save a New Superuser with given details"""
        user=self.create_user(email,name,password)   # self is not necessary to write in argument , it pass
        # automatically when we call the function in python

        user.is_superuser=True
        user.is_staff = True
        user.save(using=self._db)

        return user





class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Databases models for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)   # to identify is the user is active or not.
    is_staff  = models.BooleanField(default=False)  # for granting access to the admin panel of the website
    
    objects = UserProfileManager()
    
    """
    here we are override the USERNAME FIELD OF DJANGO admin to our custom define email model, Django Takes username
    and password for authentication, but instead of taking the username , we are taking the email address. and password
    """
    USERNAME_FIELD = 'email' # Basically we request django to overide email in place of username field in django.
    
    
    """ 
    Required fields ask to store more attribute apart from the email and password, So in this model
    django authenticate user email and password and stores an extra compulsory field  of 'name' """
    REQUIRED_FIELDS=['name']  #basically aditional required field. 
    
    #adding the couple of function for user to authenicate with the django custom model.

    def get_full_name(self):
        """Retrieve Full Name of the user"""
        return self.name

    def get_short_name(self):
        """Retreive short name of the user"""
        return self.name

    """Now this is the item that we want to return ,when we convert a user profie object to a string
    basically this lines do user profile object to..........  string"""
    def __str__(self):
        """Return String Representation Of A user profile Model"""
        return self.email   # basically help to identify this model in the django admin panel
     

    






    

