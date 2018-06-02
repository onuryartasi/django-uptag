from django.shortcuts import render, HttpResponse,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello</h1>')


class Home(View):
    initial = {'key': 'value'}
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Anasayfa'})

class Login(View):
    initial = {'key': 'value'}
    template_name = 'login.html'



    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name, {'title': 'Login'})



    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return render(request, self.template_name, {'title': 'Login'})




class Create_User(LoginRequiredMixin,View):
    login_url = '/login'
    template_name = 'create_user.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Anasayfa'})




def logout_view(request):
    logout(request)
    return redirect('home')