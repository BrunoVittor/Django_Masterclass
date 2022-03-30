from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact


# Create your views here.

def index(request):
	contex = {
		'contacts': Contact.objects.all().order_by('name')
	}
	return render(request, 'posts/index.html', contex)


def detail_index(request, id):
	contact = get_object_or_404(Contact, id=id)
	context = {
		'contact': contact
	}
	return render(request, 'posts/detail_index.html', context)


@login_required(login_url='/')
def create_contact(request):
	form = ContactForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		contact = form.save()
		return HttpResponseRedirect(contact.get_absolute_url())
	context = {
		'form': form
	}
	return render(request, 'posts/create.html', context)


@login_required(login_url='/')
def delete_contact(request, id):
	contact = get_object_or_404(Contact, id=id)
	contact.delete()
	return redirect('/')


def update_contact(request, id):
	contact = get_object_or_404(Contact, id=id)
	form = ContactForm(request.POST or None, request.FILES or None, instance=contact)
	if form.is_valid():
		contact.save()
		return HttpResponseRedirect(contact.get_absolute_url())
	context = {
		'form': form
	}
	return render(request, 'posts/create.html', context)
