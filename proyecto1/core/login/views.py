import uuid

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, RedirectView

from config import settings
from core.login.forms import ResetPasswordForm, ChangePasswordForm

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string

from config import settings
from core.user.models import User


class loginFormView(LoginView):
    template_name = 'login/login.html'


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesion'
        return context



class loginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesion'
        return context


class logoutFormView(RedirectView):
    pattern_name = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'login/resetpwd.html'
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def send_email_reset_password(self, user):
        data = {}
        try:
            URL = settings.DOMAIN if not settings.DEBUG else self.request.META['HTTP_HOST']

            user.token = uuid.uuid4()
            user.save()

            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            mailServer.starttls()
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            
            email_to = user.email
            
            # Construimos el mensaje simple
            mensaje = MIMEMultipart()
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = email_to
            mensaje['Subject'] = "Reseteo de password"
            
            content = render_to_string('login/send_email.html',{
                'user': user,
                'link_resetpwd': 'http://{}/login/change/password/{}/'.format(URL, str(user.token)),
                'link_home': 'http://{}'.format(URL)
            })
            mensaje.attach(MIMEText(content, 'html'))
            
            mailServer.sendmail(settings.EMAIL_HOST_USER, 
                                email_to, 
                                mensaje.as_string())
            print('Correo enviado correctamente')
        except Exception as e:
            data['error'] = str(e)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                user = form.get_user()
                data = self.send_email_reset_password(user)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo del Password'
        return context

class ChangePasswordView(FormView):
    form_class = ChangePasswordForm
    template_name = 'login/changepwd.html'
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        token = self.kwargs['token']
        if User.objects.filter(token=token).exists():
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect('/')


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                user = User.objects.get(token=self.kwargs['token'])
                user.set_password(request.POST['password'])
                user.token = uuid.uuid4()
                user.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo del Password'
        context['login_url'] = settings.LOGIN_URL
        return context
