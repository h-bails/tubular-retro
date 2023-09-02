from django.db import models


class Consignment(models.Model):
    '''Model for a consignment request'''
    class Status(models.TextChoices):
        SUBMITTED = "1", "Submitted"
        APPROVED = "2", "Approved"
        DECLINED = "3", "Declined"

    name = models.CharField(max_length=254)
    description = models.TextField(max_length=1000)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, 
                                     null=True, blank=True, related_name='consignments')
    date_submitted = models.DateField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SUBMITTED,
    )
    image_1 = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-date_submitted']

    def __str__(self):
        return self.name

    
