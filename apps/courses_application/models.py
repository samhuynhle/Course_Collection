from django.db import models

#validator
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 5:
            errors['title'] = "Course title should be more than 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Course description should more than 15 characters"

        return errors

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['comment']) < 15:
            errors['comment'] = "Course comment should more than 15 characters"

        return errors

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    
    def __repr__(self):
        return f"<Course object: {self.title} ({self.id})>"

class Comment(models.Model):
    username = models.CharField(max_length=55)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, related_name="comments")
    objects = CommentManager()

    def __repr__(self):
        return f"<Comment object: {self.id}>"