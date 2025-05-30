from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage

def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def contact(request):
    return render(request, 'portfolio/contact.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            message = form.save()
            
            # Send email notification
            send_mail(
                subject=f"New contact form submission from {message.name}",
                message=message.message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form})