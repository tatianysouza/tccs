from django.urls import path
from .views import *

urlpatterns = [
    path('', LivrosPublicadoList.as_view(), name='index'),
    path('dashboard/livros/', LivrosListPorUsuario.as_view(), name='listar_livros_usuario'),
    path('listar/livros_autor/<int:autor>/', LivrosAutorList.as_view(), name='listar_livros_autor'),
    path('listar/livros_editora/<int:curso>/', LivrosEditoraList.as_view(), name='listar_livros_editora'),
    path('listar/tccs_orientador/<int:orientador>/', TccsPorOrientadorList.as_view(), name='listar_tccs_orientador'),
    path('detalhar/livro/<int:pk>/', LivroDetail.as_view(), name='detalhar_livro'),
    path('livro/<int:pk>/', LivroDetailPublicado.as_view(), name='detalhar_livro_publicado'),
    path('criar/livro/', LivroCreate.as_view(), name='criar_livro'),
    path('editar/livro/<int:pk>/', LivroUpdate.as_view(), name='editar_livro'),
    path('deletar/livro/<int:pk>/', LivroDelete.as_view(), name='deletar_livro'),

    path('criar/autor/', AutorCreate.as_view(), name='criar_autor'),
    path('editar/autor/<int:pk>/', AutorUpdate.as_view(), name='editar_autor'),
    path('deletar/autor/<int:pk>/', AutorDelete.as_view(), name='deletar_autor'),
    path('listar/autores/', AutorList.as_view(), name='listar_autores'),
    path('detalhar/autor/<int:pk>/', AutorDetail.as_view(), name='detalhar_autor'),
    path('autor/<int:pk>/', AutorDetailPublicado.as_view(), name='detalhar_autor_publicado'),

    path('criar/editora/', EditoraCreate.as_view(), name='criar_editora'),
    path('editar/editora/<int:pk>/', EditoraUpdate.as_view(), name='editar_editora'),
    path('deletar/editora/<int:pk>/', EditoraDelete.as_view(), name='deletar_editora'),
    path('listar/editoras/', EditoraList.as_view(), name='listar_editoras'),

    path('criar/orientador/', OrientadorCreate.as_view(), name='criar_orientador'),
    path('editar/orientador/<int:pk>/', OrientadorUpdate.as_view(), name='editar_orientador'),
    path('deletar/orientador/<int:pk>/', OrientadorDelete.as_view(), name='deletar_orientador'),
    path('listar/orientador/', OrientadorList.as_view(), name='listar_orientadores'),
]