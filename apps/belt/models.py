from __future__ import unicode_literals
import re
import bcrypt
from django.db import models



class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        my_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 3:
            errors['first_name'] = "first_name name must be at least 3 characters"

        if len(postData['last_name']) < 1:
            errors['last_name'] = "last_name name must be at least 1 characters"

        if not my_re.match(postData['email']):
            errors['email'] = " enter a valid email id"

        if postData['password'] != postData['confirm_password']:
            errors['password'] = "passwords must match"

        return errors

    def validateLogin(self, postData):
        errors = {}
        my_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        hash2 = postData['password'].encode()
       
        if not my_re.match(postData['email']):
            errors['email'] = "Enter a valid email id"
        else :
            # try:
            try :
                user = User.objects.get(email = postData['email'])
                print "user  ", user
                if (user):
                    if bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
                       
                        print "logged in"
                    else :
                            errors['password'] = "password do not match"
                       
            except :
            # User.DoesNotExist:
           
                errors['emailnotexist']="email doesn't exist"
                print "user not found"
               
        print errors
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "User: \n{}\n{}\n{}\n{}\n".format(self.id, self.first_name, self.password, self.email)
    def __str__(self):
        return "User: \n{}\n{}\n{}\n{}\n".format(self.id, self.first_name, self.password, self.email)

