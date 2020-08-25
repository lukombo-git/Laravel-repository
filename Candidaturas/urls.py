from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.static import serve
from . import views
from django.conf import settings
import debug_toolbar


from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from .api import CandidatesViewSet,VagasViewSet


router = DefaultRouter()
router.register(r'candidates',CandidatesViewSet)
router.register(r'vagas',VagasViewSet)


urlpatterns = [
    path('unitel_endpoint', include(router.urls)),

    path("register/", views.UserRegister,name='register'),
    path("login/", views.UserLogin,name='login'),
    path("logout/", views.UserLogout,name='logout'),

    path("profile_edit/", views.UserEditProfile, name='profile_edit'),
    path("user_profile/", views.UserProfile, name='user_profile'),
    path("user_change_password/", views.UserChangePassword, name='user_change_password'),

    path("register_candidates/", views.RegisterCandidates, name='register_candidates'),
    path("list_candidates/", views.ListCandidates, name='list_candidates'),
    path("candidates_view/<str:pk>/", views.CandidatesView, name='candidates_view'),
    path("candidate_delete/<str:pk>/", views.CandidatesDelete, name='candidate_delete'),
    path("search", views.SearchView, name='search'),
    path("candidate_classification", views.CandidateClassification, name='candidate_classification'),

    path("register_vagas/", views.RegisterVagas, name='register_vagas'),
    path("list_vagas/", views.ListVagas, name='list_vagas'),
    path("vaga_view/<str:pk>/", views.VagasView, name='vaga_view'),
    path("vaga_delete/<str:pk>/", views.VagasDelete, name='vaga_delete'),

    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(template_name='Candidaturas/password_change_done.html'), name='password_change_complete'),
    path("password_change/",auth_views.PasswordChangeView.as_view(template_name='Candidaturas/password_change.html'), name='password_change'),
    
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name='Candidaturas/password_reset.html'), name='password_reset'),
    path("password_reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name='Candidaturas/password_reset_done.html'), name='password_reset_done'),
    path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name='Candidaturas/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name='Candidaturas/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns +=path('__debug__/', include(debug_toolbar.urls)),
