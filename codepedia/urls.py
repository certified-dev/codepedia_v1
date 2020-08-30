from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from core import views

urlpatterns = [
    path("update_server/", views.update, name="update"),

    path("select2/", include("django_select2.urls")),

    path('answer/<int:pk>/accept/', views.accept, name="accept_answer"),

    path('', views.home, name="home"),

    path('home/', views.HomeQuestionView.as_view(), name="home_question"),

    path('questions/', views.QuestionListView.as_view(), name="question"),

    path('question/<int:pk>/<slug:slug>/',
         views.AnswerListView.as_view(), name="question_detail"),

    path('question/ask/', views.QuestionCreateView.as_view(), name="ask_question"),

    path('question/<int:pk>/<slug:slug>/update/',
         views.QuestionUpdateView.as_view(), name="update_question"),

    path('question/<int:pk>/<slug:slug>/reply/',
         views.reply_question, name="reply_question"),

    path('question/answer/<int:pk>/reply/',
         views.reply_answer, name="reply_answer"),

    path('question/<int:pk>/answer/<int:answer_pk>/update/',
         views.AnswerUpdateView.as_view(), name="update_answer"),

    path('question/answer/<int:pk>/delete/',
         views.delete_answer, name="delete_answer"),

    path('question/<int:pk>/<slug:slug>/vote/',
         views.vote_question, name="vote_question"),

    path('answer/<int:pk>/vote/',
         views.vote_answer, name="vote_answer"),

    path('users/',
         views.UsersListView.as_view(), name="users"),

    path('user/<int:pk>/',
         views.UserDetailView.as_view(), name="user"),

    path('user/<int:pk>/update/',
         views.UserUpdateView.as_view(), name="user_update"),

    path('tags/', views.TagListView.as_view(), name="tags"),

    path('tagged/<int:pk>/questions/',
         views.TagQuestionView.as_view(), name="tag_question"),

    path('accounts/', include('allauth.urls')),

    path('', include('pagedown.urls')),

    path('admin/', admin.site.urls)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
