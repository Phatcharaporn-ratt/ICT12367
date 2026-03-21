from django.shortcuts import render, redirect
from myapp.models import Person

def index(request):
    all_person_data = Person.objects.all()
    return render(request, 'index.html', {'all_person': all_person_data})


def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        Person.objects.create(
            name=name,
            age=age
        )

        return redirect("/")

    return render(request, "form.html")