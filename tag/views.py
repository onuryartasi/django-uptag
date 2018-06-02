from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout
from tag.models  import User

# Create your views here.

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
            redirect_to=request.GET.get('redirect_to')
            if redirect_to and redirect_to.strip():
                return HttpResponseRedirect(request.GET.get('redirect_to'))
            return redirect('home')
        return render(request, self.template_name, {'title': 'Login'})


class Create_User(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ="redirect_to"
    template_name = 'create_user.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Create user'})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        ssh_key=request.POST['ssh_key']
        user=User(username=username,password=password,ssh_key=ssh_key)
        user.save()
        return redirect('home')

class Create_Project(LoginRequiredMixin,View):
    login_url = '/login'
    redirect_field_name ="redirect_to"
    template_name = 'create_project.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'Create Project'})



def logout_view(request):
    logout(request)
    return redirect('home')