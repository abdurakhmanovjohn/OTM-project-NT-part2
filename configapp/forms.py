from django import forms
from .models import OTM, Group, Student

class OTMForm(forms.ModelForm):
  class Meta:
    model = OTM
    fields = ["otm_name", "otm_email", "otm_phone_number", "otm_address"]


class GroupForm(forms.ModelForm):
  class Meta:
    model = Group
    fields = ["group_name", "group_field", "otm"]


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = [
      "student_f_name",
      "student_l_name",
      "student_email",
      "student_phone_number",
      "student_birth_year",
      "student_image",
      "group",
    ]