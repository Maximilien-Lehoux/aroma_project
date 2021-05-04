from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def contact(request):
    """contact form that sends the message entered by the user"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'maximilien.lehoux.pro@gmail.com',
                          ['maximilien.lehoux.pro@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("user:contact")

    form = ContactForm()
    return render(request, "user/contact.html", {'form': form})
