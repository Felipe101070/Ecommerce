from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

def home_page(request):
    context = {
                "title": "Stip Store",
                "content": "Seja bem vindo a essa familia",
              }
    if request.user.is_authenticated:
        context["premium_content"] = "Seja bem vindo a essa familia"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
                "title": "Pagina Sobre",
                "content": "Venha conhecer um pouco mais sobre nós!!!"
              }
    return render(request, "about/view.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
                "title": "Pagina de contato",
                "content": "Bem vindo a nossa pagina de contato",
                "form": contact_form
              }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)
