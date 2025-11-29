from django.shortcuts import render, redirect, get_object_or_404
from .models import OTM, Group, Student
from .forms import OTMForm, GroupForm, StudentForm

def index(request):
    return render(request, "index.html")


# ----------------------- OTM -----------------------

def otm_list(request):
    otms = OTM.objects.all()
    return render(request, "otm_list.html", {"otms": otms})


# def otm_add(request):
#     if request.method == "POST":
#         OTM.objects.create(
#             otm_name=request.POST["name"],
#             otm_email=request.POST["email"],
#             otm_phone_number=request.POST["phone"],
#             otm_address=request.POST["address"],
#         )
#         return redirect("configapp:otm_list")
#     return render(request, "otm_form.html")

def otm_add(request):
    if request.method == "POST":
        form = OTMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("configapp:otm_list")
    else:
        form = OTMForm()

    return render(request, "otm_form.html", {"form": form})


# def otm_edit(request, pk):
#     otm = get_object_or_404(OTM, pk=pk)

#     if request.method == "POST":
#         otm.otm_name = request.POST["name"]
#         otm.otm_email = request.POST["email"]
#         otm.otm_phone_number = request.POST["phone"]
#         otm.otm_address = request.POST["address"]
#         otm.save()
#         return redirect("configapp:otm_list")

#     return render(request, "otm_form.html", {"otm": otm})

def otm_edit(request, pk):
    otm = get_object_or_404(OTM, pk=pk)

    if request.method == "POST":
        form = OTMForm(request.POST, instance=otm)
        if form.is_valid():
            form.save()
            return redirect("configapp:otm_list")
    else:
        form = OTMForm(instance=otm)

    return render(request, "otm_form.html", {"form": form})

def otm_delete(request, pk):
    otm = get_object_or_404(OTM, pk=pk)
    otm.delete()
    return redirect("configapp:otm_list")


# ----------------------- GROUP -----------------------

def group_list(request):
    groups = Group.objects.all()
    return render(request, "group_list.html", {"groups": groups})


# def group_add(request):
#     otms = OTM.objects.all()

#     if request.method == "POST":
#         Group.objects.create(
#             group_name=request.POST["name"],
#             group_field=request.POST["field"],
#             otm_id=request.POST["otm"]
#         )
#         return redirect("configapp:group_list")

#     return render(request, "group_form.html", {"otms": otms})

def group_add(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("configapp:group_list")
    else:
        form = GroupForm()

    return render(request, "group_form.html", {"form": form})


# def group_edit(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     otms = OTM.objects.all()

#     if request.method == "POST":
#         group.group_name = request.POST["name"]
#         group.group_field = request.POST["field"]
#         group.otm_id = request.POST["otm"]
#         group.save()
#         return redirect("configapp:group_list")

#     return render(request, "group_form.html", {"group": group, "otms": otms})

def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect("configapp:group_list")
    else:
        form = GroupForm(instance=group)

    return render(request, "group_form.html", {"form": form})


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect("configapp:group_list")


# ----------------------- STUDENT -----------------------

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


# def student_add(request):
#     groups = Group.objects.all()

#     if request.method == "POST":
#         Student.objects.create(
#             student_f_name=request.POST["fname"],
#             student_l_name=request.POST["lname"],
#             student_email=request.POST["email"],
#             student_phone_number=request.POST["phone"],
#             student_birth_year=request.POST["birth"],
#             student_image=request.FILES.get("image"),
#             group_id=request.POST["group"]
#         )
#         return redirect("configapp:student_list")

#     return render(request, "student_form.html", {"groups": groups})

def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("configapp:student_list")
    else:
        form = StudentForm()

    return render(request, "student_form.html", {"form": form})


# def student_edit(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     groups = Group.objects.all()

#     if request.method == "POST":
#         student.student_f_name = request.POST["fname"]
#         student.student_l_name = request.POST["lname"]
#         student.student_email = request.POST["email"]
#         student.student_phone_number = request.POST["phone"]
#         student.student_birth_year = request.POST["birth"]

#         if request.FILES.get("image"):
#             student.student_image = request.FILES["image"]

#         student.group_id = request.POST["group"]
#         student.save()

#         return redirect("configapp:student_list")

#     return render(request, "student_form.html", {"student": student, "groups": groups})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("configapp:student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "student_form.html", {"form": form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("configapp:student_list")


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "student_detail.html", {"student": student})