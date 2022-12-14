from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from apps.livros.models import Livro, Autor, Editora, Orientador
from apps.livros.form import LivroForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages

class LivroCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = LivroForm
    success_message = 'TCC cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_livros_usuario")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'TCC`S'
        context['descricao'] = 'Cadastro de TCC'
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class LivroUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Livro
    form_class = LivroForm
    success_message = 'TCC atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_livros_usuario")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'TCC`S'
        context['descricao'] = 'Editar TCC'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class LivroDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Livro
    success_message = 'TCC excluído com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_livros_usuario")

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'TCC`S'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(LivroDelete, self).delete(request, *args, **kwargs)

class LivroDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Livro
    template_name = "cadastros/detalhes/livro.html"

class LivroDetailPublicado(DetailView):
    model = Livro
    template_name = "cadastros/detalhes/livro.html"

class LivrosListPorUsuario(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Livro
    template_name = "cadastros/listas/dashboard.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return Livro.objects.filter(usuario=self.request.user, titulo__icontains=nome)
        else:
            return Livro.objects.filter(usuario=self.request.user)

class LivrosPublicadoList(ListView):
    model = Livro
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return Livro.objects.filter(publicado=True, titulo__icontains=nome)
        else:
            return Livro.objects.filter(publicado=True)

class LivrosAutorList(ListView):
    model = Livro
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return Livro.objects.filter(publicado=True, autor=Autor.objects.get(pk=self.kwargs['autor']), titulo__icontains=nome)
        else:
            return Livro.objects.filter(publicado=True, autor=Autor.objects.get(pk=self.kwargs['autor']))

class AutorDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Autor
    template_name = "cadastros/detalhes/autor.html"

class AutorDetailPublicado(DetailView):
    model = Autor
    template_name = "cadastros/detalhes/autor.html"

class LivrosEditoraList(ListView):
    model = Livro
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return Livro.objects.filter(publicado=True, curso=Editora.objects.get(pk=self.kwargs['curso']), titulo__icontains=nome)
        else:
            return Livro.objects.filter(publicado=True, curso=Editora.objects.get(pk=self.kwargs['curso']))

class LivrosOrientadorList(ListView):
    model = Livro
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):
        nome = self.request.GET.get('nome')

        if nome:
            return Livro.objects.filter(publicado=True, orientador=Orientador.objects.get(pk=self.kwargs['orientador']), titulo__icontains=nome)
        else:
            return Livro.objects.filter(publicado=True, orientador=Orientador.objects.get(pk=self.kwargs['orientador']))