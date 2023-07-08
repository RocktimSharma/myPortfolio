# Create your views here.
from django.shortcuts import render
from .forms import *
from django.core.mail import mail_admins, EmailMessage
from .admin import Social, Projects, MyInfo, Skills

from django.template import RequestContext


# -------------------------------------------Method to render Home Page----------------------------------------------- #
def splash(request):
    return render(request, 'index.html')


def home(request):
    success = False
    fail = False
    socials = Social.objects.all()
    myInfo = MyInfo.objects.all()
    skills = Skills.objects.all()

    if not myInfo:
        return render(request, 'error.html')

    try:
        recentproject = Projects.objects.filter(pin=True).first()
        images = recentproject.images.split(',')
        tools = recentproject.tools.split(',')
        lang = recentproject.language.split(',')
        points = recentproject.keyPoints.replace('\r', '\n').split('\n\n\n')
        recentproject.images = images
        recentproject.tools = tools
        recentproject.language = lang
        recentproject.keyPoints = points
    except:
        recentprojects = Projects.objects.all().first()

    if request.method == 'POST':  # Checking if the request method is POST
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]  # Getting the Enter Name in Contact Form
            email = form.cleaned_data["email"]  # Getting the Enter Email in Contact Form
            message = form.cleaned_data["message"]  # Getting the Enter Message in Contact Form
            subject = 'Portfolio Mail'  # Mail Subject
            email_text = f'Name: {name} \nEmail: {email} \n\nMessage: \n {message}'  # Concatenating the email message
            try:
                context = {
                    'recipient_name': name,
                    'name': name,
                    'email': email,
                    'message': message
                }
                # Render the email template with the context
                email_content = render(request, 'email_template.html', context).content.decode('utf-8')
                # Send the email
                email_message = EmailMessage('Thank you for your inquiry', email_content, 'dummymail58536@gmail.com',
                                             [email])
                email_message.content_subtype = 'html'  # Set the content subtype as HTML
                email_message.send()
                mail_admins(subject, email_text, fail_silently=False, connection=None, html_message=None)
                success = True
            except:
                fail = True

            return render(request, 'home.html',
                          context={'form': form, 'success': success, 'fail': fail, 'socials': socials,
                                   'myInfo': myInfo[0], 'recent': recentproject, 'skills': skills})

    else:
        form = ContactForm()  # Initializing ContactForm class
        return render(request, 'home.html',
                      context={'form': form, 'socials': socials, 'myInfo': myInfo[0], 'recent': recentproject,
                               'skills': skills})


# ----------------------------------------Method to render Certificate Page------------------------------------------- #
def allWorks(request):
    projects = Projects.objects.all()
    if not projects:
        return render(request, 'error.html')
    for project in projects:
        images = project.images.split(',')
        tools = project.tools.split(',')
        lang = project.language.split(',')
        points = project.keyPoints.replace('\r', '\n').split('\n\n\n')
        project.images = images
        project.tools = tools
        project.language = lang
        project.keyPoints = points
    return render(request, 'work.html', context={'works': projects})


def error_400(request, *args, **kwargs):
    return render('error.html', status=400)


def error_403(request, *args, **kwargs):
    return render('error.html', status=403)


def error_404(request, *args, **kwargs):
    return render('error.html', status=404)


def handle500(request, *args, **kwargs):
    return render(request, 'error.html', status=500)
