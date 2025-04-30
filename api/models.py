from django.db import models

class Post(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  content = models.TextField()
  category = models.CharField(max_length=100, blank=True, null=True)
  tags = models.JSONField(default=list)

  def __str__(self):
    return self.title
