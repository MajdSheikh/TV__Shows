from django.shortcuts import render, redirect
from .models import Show

def index(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, 'index.html', context)



def shows_new(request):
    return render(request, 'shows_new.html')



def create_shows(request):
    this_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"], 
    description=request.POST["description"],  release_date=request.POST["release_date"])

    return redirect("/shows/"+str(this_show.id)+"/")

# def display_all_shows(request):
#         Show.objects.all()

#         return redirect("/")


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

    this_show.title=request.POST['title']
    this_show.network=request.POST['network']
    this_show.release_date=request.POST['release_date']
    this_show.description=request.POST['description']
    this_show.save()

    return redirect('/shows/' + str(this_show.id))

def destroy_show(request, show_id):
    this_show = Show.objects.get(id=show_id)
    this_show.delete()

    return redirect("/")

