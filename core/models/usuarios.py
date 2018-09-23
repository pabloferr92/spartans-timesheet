from django.db import models

class Users(models.Model):
    ulogin = models.CharField(db_column='uLogin')
    userid = models.IntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

    
    def __str__(self):
        return self.ulogin