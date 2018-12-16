from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.text import slugify
import random
from string import ascii_lowercase

# Create your models here.
class EmployeeProfileManager(UserManager):
    pass


def image_upload_to(instance, filename):
    emp_name = instance.first_name + instance.last_name
    slug = slugify(emp_name)
    special_code = [(str(random.randint(0, 10)) + random.choice(ascii_lowercase)) for i in range(2)]
    base_name, file_extension = filename.split(".")
    new_filename = "%s-%s.%s" %(slug, special_code, file_extension)
    return "employee_profiles/%s/%s" %(slug, new_filename)

class EmployeeProfile(AbstractUser):
    employee_type = models.CharField(max_length=2)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to=image_upload_to, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    joining_date = models.DateTimeField(null=True, blank=True)
    leaving_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    objects = EmployeeProfileManager()

    @property
    def is_restaurant_manager(self):
        if self.employee_type == 'RM':
            return True
        return False

    @property
    def is_table_manager(self):
        if self.employee_type == 'TM':
            return True
        return False

    @property
    def is_kitchen_manager(self):
        if self.employee_type == 'KM':
            return True
        return False

    @property
    def is_shef(self):
        if self.employee_type == 'SF':
            return True
        return False
