from django.db import models


class ShowManager(models.Manager):
     def basic_validator(self, postData):
        errors = {}

        # if len (postData['title']) or len(postData['network']) or len(postData['description']) == 0:
        #     errors['key'] = "you need to fill all fileds"
        if len(postData['title']) < 2:
            errors["title"] = "TV show title should be at least 2 characters"

        if len(postData['network']) < 3:
            errors["network"] = "TV show network should be at least 3 characters"
    
        if len(postData['description']) < 10:
            errors["description"] = "TV show description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 
