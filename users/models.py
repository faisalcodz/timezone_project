from django.db import models
class DummyUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pakistan_time = models.DateTimeField()
    utc_time = models.DateTimeField(null=True, blank=True)
    converted_back_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name