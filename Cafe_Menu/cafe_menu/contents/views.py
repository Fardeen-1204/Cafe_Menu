from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    description = home_text.objects.first()
    hot= hot_menu.objects.all()
    cold= cold_menu.objects.all()
    desert= desert_menu.objects.all()
    about= about_us.objects.first()
    contact_me = contact_details.objects.first()
    context={"desc":description,"hot":hot,"cold":cold,"desert":desert,"about":about,"contact":contact_me}
    return render(request, 'index.html',context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_form.objects.create(name=name, email=email, message=message).save()
        return redirect('index')

    return redirect(request, 'index')