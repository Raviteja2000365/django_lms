from django.db import models



class Courses(models.Model):
    course_name=models.CharField(max_length=100)
    date=models.DateTimeField(max_length=200,auto_now_add=True)
    def __str__(self):
        return self.course_name
    
    
class assignments(models.Model):
    assignment_name=models.CharField(max_length=100)
    date=models.DateTimeField(max_length=200,auto_now_add=True)
    def __str__(self):
        return self.assignment_name
    
class announcements(models.Model):
    announcement_name=models.CharField(max_length=100)
    date=models.DateTimeField(max_length=200,auto_now_add=True)
    def __str__(self):
        return self.announcement_name
   
    
class quiz(models.Model):
    quiz=models.CharField(max_length=200)
    date=models.DateTimeField(max_length=200,auto_now_add=True)
    
    def __str__(self):
        return self.quiz      
    