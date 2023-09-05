from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    Model for a contact form
    """
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    date_submitted = models.DateField(auto_now=True)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE, related_name='contacts')
    from_email = models.EmailField()

    def __str__(self):
        return self.subject
