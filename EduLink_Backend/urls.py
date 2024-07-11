"""
URL configuration for EduLink_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_base import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #  ! user
    path('Chercheur/GetAll', views.getAllUsers),
    path('Chercheur/Check', views.CheckUserCreds),
    path('Admin/Check', views.CheckAdminCreds),
    path('Chercheur/Add', views.createChercheur),
    path('User/Delete/<int:id>', views.DeleteChercheurById),

    path('Editeur/Add', views.createEditor),
    path('Editeur/Check', views.CheckEditorCreds),

    #  ! article
    path('Article/Add', views.createArticle),
    path('Article/Get', views.getArticle),
    path('Article/nAPP/Get', views.getNotApprovedArticles),
    path('Article/Get/<str:search_term>', views.getArticlebySearch),
    path('Article/Approuve', views.Approuvearticle),
    path('Article/Delete', views.DeleteArticle),

    #  ! journal
    path('Journal/Add', views.createJournal),
    path('Journal/Get', views.getJournal),
    path('Journal/GetALL', views.getJournalALL),


    #  ! Stats
    path('Stats/Get', views.getStats),

    # ! Messagerie
    path('Message/Create', views.createMessage),
    path('Message/Get', views.getMessage),

    path('Conversation/Create', views.createConversation),
]
