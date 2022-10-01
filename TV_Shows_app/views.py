from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

def index(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, 'index.html', context)



def shows_new(request):
    return render(request, 'shows_new.html')



def create_shows(request):
    if request.method =='POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/new/")

        else:

            this_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"], 
            description=request.POST["description"],  release_date=request.POST["release_date"])
            messages.success(request, "Show successfully created")

            return redirect("/shows/" + str(this_show.id) + "/")



def display_shows(request, show_id):
    context={
        "this_show":Show.objects.get(id=show_id),
    }
    return render(request,"display_shows.html", context)


def edit_show(request, show_id):
    context={
        "this_show":Show.objects.get(id=show_id),
        "this_show_release_date":Show.objects.get(id=show_id).release_date.strftime('%Y-%m-%d'),
    }
    return render(request,"edit_show.html",context)


def update_show(request, show_id):
    this_show = Show.objects.get(id=show_id)
    if request.method=='POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/" + str(this_show.id) + "/edit")

        else:

            this_show.title=request.POST['title']
            this_show.network=request.POST['network']
            this_show.release_date=request.POST['release_date']
            this_show.description=request.POST['description']
            this_show.save()
            messages.success(request, "Show successfully updated")

            return redirect('/shows/' + str(this_show.id))

def destroy_show(request, show_id):
    this_show = Show.objects.get(id=show_id)
    this_show.delete()

    return redirect("/")

