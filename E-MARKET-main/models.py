from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
        
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

class table(models.Model):
    def __str__(self):
        return self.user_name
    user_name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200,default=0)
    phn=models.CharField(max_length=200,default=0)

class farmer(models.Model):
    def __str__(self):
        return self.user_name
    user_name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.CharField(max_length=200,default=0)
    phn=models.CharField(max_length=200,default=0)
class verif(models.Model):
    def _str_(self):
        return self.user_name
    user_name=models.CharField(max_length=200)
    user_id=models.CharField(max_length=200)
