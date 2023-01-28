"""kelas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import *

def index(request):
    titelnya="About, Roadmaps, Details"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'index.html', konteks)

def base(request):
    titelnya="About, Roadmaps, Details"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'content.html', konteks)

def portfolio1(request):
    titelnya="Portfolio"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'portfoliotact.html', konteks)

def portfolio2(request):
    titelnya="Portfolio"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'portfoliozwei.html', konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('base/', base),
    path('portfoliotact/', portfolio1),
    path('portfoliozwei/', portfolio2),
    path('addbrg/', tambah_barang),
    path('items/', Barang_View),
    path('addmem/', tambah_membership),
    path('memberships/', Membership_View),
    path('ubahbrg/<int:id_barang>', ubah_brg, name = 'ubah_brg'),
    path('hapusbrg/<int:id_barang>', hapus_brg, name='hapus_brg'),
    path('ubahmem/<int:id_member>', ubah_mem, name = 'ubah_mem'),
    path('hapusmem/<int:id_member>', hapus_mem, name='hapus_mem'),
]
