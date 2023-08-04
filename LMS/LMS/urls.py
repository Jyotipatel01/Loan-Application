"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from courses import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',views.index,name='home'),
    # path('about/',views.about,name='about'),
    # #path('about/<int:id>/',views.about),
    # path('contact/',views.contact,name='contact'),
    # path('mobile/',views.mobile,name='mobile'),
    # path('courses/',views.courses,name='courses'),
    # path('save_courses/',views.save_courses)
    path('',views.get_name),
#    path('',views.ur),
    
    
    
]

