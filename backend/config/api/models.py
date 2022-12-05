from django.db import models

class Unit(models.Model):
    unit_id = models.IntegerField()
    unit_name = models.TextField()
    topics = models.JSONField()

    def __str__(self):
        return self.unit_name 
    
class Topic(models.Model):
    topic_id = models.IntegerField()
    topic_name = models.CharField(max_length=255)
    contents = models.JSONField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.topic_name
    
class Content(models.Model):
    paragraph_id = models.IntegerField()
    text = models.TextField()
    question = models.TextField()
    alt_question = models.TextField()
    keywords = models.TextField()
    intro = models.TextField()
    outro = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text
