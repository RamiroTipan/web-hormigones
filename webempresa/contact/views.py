from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm



def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # if all ok
            # Sen email and redirect
            email = EmailMessage(
                "Hormigones Ecuador: Nuevo mensaje de contacto", #subjet,
                 "De {} <{}>\n\nEscribió\n\n{}".format(name, email, content), #body,
                 "no-contestar@gmail.com",#source_email,
                 ["jramirot@hotmail.com"],#target_email,
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")

            except:
                # Error
                return redirect(reverse('contact')+"?fail")

    return render(request,'contact/contact.html', {'form': contact_form})

