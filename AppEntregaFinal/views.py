from django.shortcuts import render,redirect
from .models import Blogs
from .forms import UserCreationFormCustom, UserEditForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def blogs_list(request):
    blogs = Blogs.objects.all()
    print(blogs)
    return render(request, "blogs.html", {"blogs" : blogs})

class BlogsCreateView(CreateView):
    model = Blogs
    template_name = "crear_blogs.html"
    success_url = reverse_lazy("blogs_list")
    fields = ["titulo", "subtitulo", "descripcion", "autor", "fecha", "imagen"]

class BlogsDetailView(DetailView):
    model = Blogs
    template_name = "detalle_blog.html"

class BlogsListView(ListView):
    model = Blogs
    template_name = "blogs.html"
    context_object_name = "blogs"

class BlogsUpdateView(UpdateView):
    model = Blogs
    template_name = "editar_blog.html"
    success_url = reverse_lazy("blogs_list")
    fields = ["titulo", "subtitulo", "descripcion", "autor", "fecha", "imagen"]

class BlogsDeleteView(DeleteView):
    model = Blogs
    template_name = "eliminar_blog.html"
    success_url = reverse_lazy("blogs_list")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("inicio")
        else:
            # Manejo de error de inicio de sesión
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    return render(request, 'login.html') 

def user_register(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationFormCustom()
        return render(request, 'register.html', {'form': form})      

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST, request.FILES,instance=request.user) 
        if mi_formulario.is_valid():
            if mi_formulario.cleaned_data.get("imagen"):
                usuario.avatar.imagen = mi_formulario.cleaned_data.get("imagen")
                usuario.avatar.save()
                
            mi_formulario.save()
            return redirect("inicio")
    else:
        mi_formulario = UserEditForm(initial={"imagen" : usuario.avatar.imagen} ,instance=request.user)
    return render(request, "editarPerfil.html", {"mi_formulario" : mi_formulario, "usuario" : usuario})

class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = "cambiar_contraseña.html"
    success_url = reverse_lazy("editarPerfil")

