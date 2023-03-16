"""B8_REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1 import views
from app1.urls import new_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get-student/<int:id>/',views.get_student),
    path('api/get-all-students/',views.get_all_students),
    path('api/create-student/',views.create_student),
    # CRUD operation in one function
    # path('api/all-operation/',views.all_stud_operation),
    # path('api/stud-class-api/<int:pk>/',views.StudentAPI.as_view()),
    # path('api/stud-class-api/',views.StudentAPI.as_view()),
    # path('api/func-stud-api/',views.Student_api),
    # path('api/func-stud-api/<int:pk>/',views.Student_api),

    # GenericAPIView,mixins
    path('api/stud-generic-list/',views.StudentList.as_view()),
    path('api/stud-generic-create/',views.StudentCreate.as_view()),
    path('api/stud-generic-retrieve/<int:pk>/',views.StudentRetrieve.as_view()),
    path('api/stud-generic-update/<int:pk>/',views.StudentUpdate.as_view()),
    path('api/stud-generic-partial-update/<int:pk>/',views.StudentPartialUpdate.as_view()),
    path('api/stud-generic-delete/<int:pk>/',views.StudentDelete.as_view()),
   
   # Combined mixins
    path('api/stud-generic-list-create/',views.StudentListCreate.as_view()),
    path('api/stud-generic-retrieve-update-pupdate-delete/<int:pk>/',views.StudentRetrieveUpdatePartialUpdateDelete.as_view()),
   
   # concrete api views
    path('api/stud-concrete-generic-list/',views.StudentCList.as_view()),
    path('api/stud-concrete-generic-create/',views.StudentCCreate.as_view()),
    path('api/stud-concrete-generic-retrieve/<int:pk>/',views.StudentCRetrieve.as_view()),
    path('api/stud-concrete-generic-update/<int:pk>/',views.StudentCUpdate.as_view()),
    path('api/stud-concrete-generic-delete/<int:pk>/',views.StudentCDelete.as_view()),

    # Viewset
    # path('api/stud-viewset/',views.StudentViewset.as_view()),
    # path('api/stud-viewset/<int:pk>/',views.StudentViewset.as_view()),
    
    
    
    path("api/",include(new_urlpatterns)),
    
]
