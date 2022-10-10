o
    �<c�  �                   @   s\   d Z ddlmZ ddlmZ ddlmZ ddlmZ edej	j
�edeejdd	���gZd
S )as  hackernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
�    )�admin)�path)�csrf_exempt)�GraphQLViewzadmin/zgraphql/T)ZgraphiqlN)�__doc__Zdjango.contribr   �django.urlsr   �django.views.decorators.csrfr   Zgraphene_django.viewsr   �site�urls�as_view�urlpatterns� r   r   �?C:\Users\Santhozz\Desktop\ApiRest\hackernews\hackernews\urls.py�<module>   s    �