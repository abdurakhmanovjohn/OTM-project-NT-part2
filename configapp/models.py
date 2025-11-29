from django.db import models

class OTM(models.Model):
    otm_name = models.CharField(max_length=100)
    otm_email = models.EmailField()
    otm_phone_number = models.CharField(max_length=20)
    otm_address = models.CharField(max_length=255)

    def __str__(self):
        return self.otm_name


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_field = models.CharField(max_length=100)
    otm = models.ForeignKey(OTM, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name


class Student(models.Model):
    student_f_name = models.CharField(max_length=50)
    student_l_name = models.CharField(max_length=50)
    student_email = models.EmailField()
    student_phone_number = models.CharField(max_length=20)
    student_birth_year = models.IntegerField()
    student_image = models.ImageField(upload_to='students/', blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_f_name} {self.student_l_name}"