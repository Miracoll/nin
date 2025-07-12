from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string

# Create your models here.


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class RegistrationCenter(models.Model):
    center_name = models.CharField(max_length=255)
    officer_name = models.CharField(max_length=255)
    location = models.TextField()

    def __str__(self):
        return f"{self.center_name} - {self.officer_name}"

class NINProfile(models.Model):
    nin = models.CharField(max_length=11, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=100, default='Nigeria')

    state_of_origin = models.CharField(max_length=100)
    lga_of_origin = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=255)

    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    passport_photo = models.ImageField(upload_to='nin_photos/', blank=True, null=True)
    fingerprint_reference = models.TextField(blank=True, null=True)

    registration_center = models.ForeignKey(RegistrationCenter, on_delete=models.SET_NULL, null=True)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nin} - {self.last_name} {self.first_name}"
    
    def save(self, *args, **kwargs):
        if not self.nin:
            self.nin = self._generate_unique_nin()
        super().save(*args, **kwargs)

    def _generate_unique_nin(self):
        while True:
            nin = get_random_string(length=11, allowed_chars='0123456789')
            if not NINProfile.objects.filter(nin=nin).exists():
                return nin
    
class SupportingDocument(models.Model):
    document_name = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
    document = models.ImageField(upload_to='documents', blank=None, null=None, default='noimage.jpg')

    exp_month = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    exp_year = models.IntegerField(choices=[(y, y) for y in range(2020, 2051)]) 

    nin_user = models.ForeignKey(NINProfile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.document_name
    
class Parent(models.Model):
    father_surname = models.CharField(max_length=50)
    father_first_name = models.CharField(max_length=50)
    father_middle_name = models.CharField(max_length=50, blank=True, null=True)
    father_nin = models.CharField(max_length=50, blank=True, null=True)

    mother_surname = models.CharField(max_length=50)
    mother_first_name = models.CharField(max_length=50)
    mother_middle_name = models.CharField(max_length=50, blank=True, null=True)
    mother_nin = models.CharField(max_length=50, blank=True, null=True)

    nin_user = models.OneToOneField(NINProfile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nin_user.nin} - {self.nin_user.last_name} {self.nin_user.first_name} parent"
    
class Guardian(models.Model):
    guardian_surname = models.CharField(max_length=50)
    guardian_first_name = models.CharField(max_length=50)
    guardian_middle_name = models.CharField(max_length=50, blank=True, null=True)
    guardian_nin = models.CharField(max_length=50, blank=True, null=True)

    nin_user = models.OneToOneField(NINProfile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nin_user.nin} - {self.nin_user.last_name} {self.nin_user.first_name} guardian"
    
class NextOfKin(models.Model):
    next_of_kin_surname = models.CharField(max_length=50)
    next_of_kin_first_name = models.CharField(max_length=50)
    next_of_kin_middle_name = models.CharField(max_length=50)
    next_of_kin_relationship = models.CharField(max_length=50)

    next_of_kin_country = models.CharField(max_length=50)
    next_of_kin_state = models.CharField(max_length=50)
    next_of_kin_lga = models.CharField(max_length=50)
    next_of_kin_town = models.CharField(max_length=50)
    next_of_kin_street_address = models.CharField(max_length=50)

    next_of_kin_nin = models.CharField(max_length=50)

    nin_user = models.OneToOneField(NINProfile, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nin_user.nin} - {self.nin_user.last_name} {self.nin_user.first_name} next of kin"