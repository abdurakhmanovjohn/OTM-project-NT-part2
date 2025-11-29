from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import OTM, Group, Student
from .forms import OTMForm, GroupForm, StudentForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

# def index(request):
#     return render(request, "index.html")

class IndexView(TemplateView):
    template_name = "index.html"


# ----------------------- OTM -----------------------

# def otm_list(request):
#     otms = OTM.objects.all()
#     return render(request, "otm_list.html", {"otms": otms})

class OTMListView(ListView):
    model = OTM
    template_name = "otm_list.html"
    context_object_name = "otms"

# def otm_add(request):
#     if request.method == "POST":
#         form = OTMForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("configapp:otm_list")
#     else:
#         form = OTMForm()

#     return render(request, "otm_form.html", {"form": form})

class OTMCreateView(CreateView):
    model = OTM
    form_class = OTMForm
    template_name = "otm_form.html"
    success_url = reverse_lazy("configapp:otm_list")

# def otm_edit(request, pk):
#     otm = get_object_or_404(OTM, pk=pk)

#     if request.method == "POST":
#         form = OTMForm(request.POST, instance=otm)
#         if form.is_valid():
#             form.save()
#             return redirect("configapp:otm_list")
#     else:
#         form = OTMForm(instance=otm)

#     return render(request, "otm_form.html", {"form": form})

class OTMUpdateView(UpdateView):
    model = OTM
    form_class = OTMForm
    template_name = "otm_form.html"
    success_url = reverse_lazy("configapp:otm_list")

# def otm_delete(request, pk):
#     otm = get_object_or_404(OTM, pk=pk)
#     otm.delete()
#     return redirect("configapp:otm_list")

class OTMDeleteView(DeleteView):
    model = OTM
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("configapp:otm_list")


# ----------------------- GROUP -----------------------

# def group_list(request):
#     groups = Group.objects.all()
#     return render(request, "group_list.html", {"groups": groups})

class GroupListView(ListView):
    model = Group
    template_name = "group_list.html"
    context_object_name = "groups"

# def group_add(request):
#     if request.method == "POST":
#         form = GroupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("configapp:group_list")
#     else:
#         form = GroupForm()

#     return render(request, "group_form.html", {"form": form})

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = "group_form.html"
    success_url = reverse_lazy("configapp:group_list")


# def group_edit(request, pk):
#     group = get_object_or_404(Group, pk=pk)

#     if request.method == "POST":
#         form = GroupForm(request.POST, instance=group)
#         if form.is_valid():
#             form.save()
#             return redirect("configapp:group_list")
#     else:
#         form = GroupForm(instance=group)

#     return render(request, "group_form.html", {"form": form})
class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "group_form.html"
    success_url = reverse_lazy("configapp:group_list")


# def group_delete(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     group.delete()
#     return redirect("configapp:group_list")

class GroupDeleteView(DeleteView):
    model = Group
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("configapp:group_list")


# ----------------------- STUDENT -----------------------

# def student_list(request):
#     students = Student.objects.all()
#     return render(request, "student_list.html", {"students": students})

class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"

# def student_add(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("configapp:student_list")
#     else:
#         form = StudentForm()

#     return render(request, "student_form.html", {"form": form})

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("configapp:student_list")


# def student_edit(request, pk):
#     student = get_object_or_404(Student, pk=pk)

#     if request.method == "POST":
#         form = StudentForm(request.POST, request.FILES, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect("configapp:student_list")
#     else:
#         form = StudentForm(instance=student)

#     return render(request, "student_form.html", {"form": form})

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("configapp:student_list")


# def student_delete(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     student.delete()
#     return redirect("configapp:student_list")

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("configapp:student_list")


# def student_detail(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     return render(request, "student_detail.html", {"student": student})

class StudentDetailView(DetailView):
    model = Student
    template_name = "student_detail.html"