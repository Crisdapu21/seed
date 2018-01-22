from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import *


def loginView(request):
    if request.user.is_authenticated():
        return redirect('indexWebsite')
    else:
        if 'login_form' in request.POST:
            login_form = LoginForm(request.POST)
            
            if login_form.is_valid():
                user = authenticate(username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
                if user is not None:
                    try:
                        if user.is_active:
                            login(request, user)
                            return redirect('indexWebsite')
                    except:
                        login_form = LoginForm()
                        dataErrorLogin = "Lo sentimos, su usuario no esta habilitado para ingresar al sistema"
                        return render(request, 'loginUser.html', {'login_form': login_form, 'dataErrorLogin': dataErrorLogin})
                else:
                    login_form = LoginForm()
                    dataErrorLogin = "Usuario y/o contraseña no son válidos"
                    return render(request, 'loginUser.html', {'login_form': login_form, 'dataErrorLogin': dataErrorLogin})
            else:
                raise ('Error Login : Form Invalid')
        else:
            login_form = LoginForm()
            return render(request, 'loginUser.html', {'login_form': login_form})




def registerView(request):
    if request.user.is_authenticated():
        return redirect('indexWebsite')
    else:
        if request.method == "POST":
            if 'register_form' in request.POST:
                user_register = UserRegisterForm(request.POST)
                if user_register.is_valid():
                    User.objects.create_user(
                        username=user_register.cleaned_data['username'],
                        email=user_register.cleaned_data['email'],
                        password=user_register.cleaned_data['password'],
                         
                    )

                    user = authenticate(username=user_register.cleaned_data['username'], password=user_register.cleaned_data['password'])
                    if user is not None:
                        try:
                            if user.is_active:
                                login(request, user)
                                if user.is_staff:
                                    return redirect('indexWebsite')
                                    pass
                                else:
                                    return redirect('indexWebsite')
                                    
                        except:
                            register_form = UserRegisterForm()
                            dataErrorRegister = "Lo sentimos, su usuario no esta habilitado para ingresar al sistema"
                            return render(request, 'registerUser.html', {'register_form': register_form, 'dataErrorRegister': dataErrorRegister})
                else:
                    register_form = UserRegisterForm()
                    dataErrorRegister = "Lo sentimos ya existe una cuenta registrada con estos datos"
                    return render(request, 'registerUser.html', {'register_form': register_form, 'dataErrorRegister': dataErrorRegister})
        else:
            register_form = UserRegisterForm()
            return render(request, 'registerUser.html', {'register_form': register_form})

def logoutView(request):
    logout(request)
    return redirect('/')


 
