from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from shared.models import BaseModel


class ClientType(BaseModel):
    name = models.CharField(max_length=100, blank=True)


class Dacha(BaseModel):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    popular_place = models.ForeignKey('region.PopularPlaces', on_delete=models.CASCADE, blank=True, null=True)
    facilities = models.ManyToManyField('facilities.Facilities', blank=True)
    beds_count = models.IntegerField(blank=True, null=True)
    hall_count = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE, blank=True, null=True)

    TRANSACTION_CHOICES = (
        ('sale', 'Sotuv'),
        ('rent', 'Arenda'),
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_CHOICES,
        default='rent',
        blank=False
    )

    # Updated property type field with new options
    PROPERTY_TYPE_CHOICES = (
        ('dacha', 'Dacha'),  # Default: Dacha (general term)
        ('uchastka', 'Uchastka'),  # Plot with a house
        ('dom', 'Dom'),  # House only
        ('yer', 'Yer'),  # Land only
        ('sanitorieum', 'Sanatoriya'),  # Land only
        ('hotel', 'Mehmonhona'),  # Land only
    )
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES,
        default='dacha',  # Default set to 'dacha'
        blank=False
    )


# Other models remain unchanged
class DachaImage(BaseModel):
    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dacha/')


class DachaComment(BaseModel):
    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    comment = models.TextField()


class DachaLike(BaseModel):
    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('dacha', 'user')


class DachaCommentLike(BaseModel):
    comment = models.ForeignKey(DachaComment, on_delete=models.CASCADE)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('comment', 'user')


class DachaRating(BaseModel):
    dacha = models.ForeignKey(Dacha, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('dacha', 'user')
