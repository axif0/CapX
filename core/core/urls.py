
from django.contrib import admin
from django.urls import path
from bug.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("suc-cese/", succese, name="succese"),
    path("delete-bug/<slug:slug>/", delete_bug, name="delete_bug"),
    path("update-bug/<slug:bugTitle>/", update_bug, name="update_bug"),
    path('admin/', admin.site.urls),
    
    path('leaderboard/',leaderboard, name='leaderboard'),

    path('login/',login_page,name='login'),
    path('reg/',reg_page,name='reg_page'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]

# Error handling views
handler404 = lambda request, exception: error_page(request, 404, 'Page not found')
handler500 = lambda request: error_page(request, 500, 'Server Error')
