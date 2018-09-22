from django.db import models

class Users(models.Model):
    login = models.TextField()  # This field type is a guess.
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

    
    def __str__(self):
        return self.login