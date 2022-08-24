from django.db import models

STATE_CHOICE = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chattisgarh', 'Chattisgarh'),
    ('Dadra & Nagar Havel', 'Dadra & Nagar Havel'),
    ('Diu & Daman', 'Diu & Daman'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu & Kashmir', 'Jamu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Maharashtra', 'Maharashtra'),

)


class Resume(models.Model):

    name = models.CharField(max_length=30)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=30)
    locality = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=30)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)
