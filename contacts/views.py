from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,request
from django.template import loader
from .models import Contacts
from django.views.decorators.csrf import csrf_exempt

def contacts(request):
    #displays all the contacts
    contact=Contacts.objects.all().values()
    template=loader.get_template("home.html")
    context={
        "contact":contact,
    }
    return HttpResponse(template.render(context,request))


@csrf_exempt
def add_contact(request):
    if request.method == 'GET':
    #add the new contact and redirects to contacts page
        template=loader.get_template("add_contact.html")
        return HttpResponse(template.render())
    elif request.method == 'POST':
        name = request.POST.get('name').lower()
        phoneno = request.POST.get('phone')
        error_message = None
        if len(phoneno) > 10 or len(phoneno)<10:
            error_message = "Please enter a valid contact number."
        if Contacts.objects.filter(phoneno=phoneno).exists():
            error_message = "Phone number already exists."    
        if  error_message is None:
            contact=Contacts(name=name,phoneno=phoneno)
            contact.save()   
            return redirect("contacts")
        else:
            return render(request, "add_contact.html", {"error": error_message})

def delete(request,contact_id):
    contact=get_object_or_404(Contacts,pk=contact_id)
    contact.delete()
    return redirect("/contacts/")
@csrf_exempt
def update(request,contact_id):
    contact=get_object_or_404(Contacts, pk=contact_id)
    if request.method=="POST":
        #x=Contacts.objects.all()[contact_id-1]
        name = request.POST.get('name').lower()
        phoneno = request.POST.get('phone')
        contact.name=name
        contact.phoneno=phoneno
        contact.save()
        return redirect("contacts")
    else:
        return render(request, 'update_contact.html', {'contact': contact})
def search_contact(request):
    query=request.GET.get('search','')
    if query:
        results=Contacts.objects.filter(name=query)
    else:
        results=Contacts.objects.none()
    return render(request, 'search.html', {'results': results})
def index(request):
    template=loader.get_template("main.html")
    return HttpResponse(template.render())