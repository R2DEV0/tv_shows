from django.shortcuts import render, redirect
from .models import Show

def shows(request):
# renders the main all shows overview page.
    show= Show.objects.all()
    context={
        'show' : show
    }
    return render(request, 'shows.html', context)


def show_info(request, show_id):
# shows more details on the clicked show view link.
    the_show_info= Show.objects.get(id=show_id)
    context={
        'show': the_show_info,
    }
    return render(request, 'show_info.html', context)


def add_show(request):
# renders the new show form for the user to add new shows.
    return render(request, 'new_show.html')


def submit_new_show(request):
#submit new show from form and redirect to main show page.
    show_title= request.POST['title']
    show_network= request.POST['network']
    show_release_date= request.POST['release_date']
    show_desc= request.POST['desc']

    Show.objects.create(title=show_title, network=show_network, release_date=show_release_date, desc=show_desc)
    return redirect('/')


def edit_show(request, show_id):
# update show details page. 
    the_show_info= Show.objects.get(id=show_id)
    show_id=the_show_info.id
    context={
        'show': the_show_info,
    }
    return render(request, 'edit_show.html', context)



def submit_edit(request):
# submits the updated show info.
    show_id = request.POST['show.id']
    show= Show.objects.get(id=show_id)

    show_title = request.POST['title']
    show.title = show_title
    if request.POST['title'] == "":
        pass
    else:    
        show.title = show_title
        show.save()
        
    show_network = request.POST['network']
    if request.POST['network'] == "":
        pass
    else:    
        show.network = show_network
        show.save()

    show_release_date = request.POST['release_date']
    if request.POST['release_date'] == "":
        pass
    else:
        show.release_date = show_release_date
        show.save()

    show_desc = request.POST['desc']
    if request.POST['desc'] == "":
        pass
    else:    
        show.desc = show_desc
        show.save()
        

    return redirect(f"/show_info/{show_id}")



def delete(request, show_id):
# deletes the selected show
    the_show= Show.objects.get(id=show_id)
    the_show.delete()
    return redirect('/')