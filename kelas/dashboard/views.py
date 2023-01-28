from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.forms import FormMembership
from dashboard.models import Barang
from dashboard.models import Membership
from django.contrib import messages
from django.shortcuts import redirect


def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html', konteks)

def tambah_barang(request):
    if request.POST:
        form = FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form' : form,
            }
            return render(request, 'tambah_barang.html', konteks)
    else:

        form=FormBarang()
        konteks={
            'form':form,
        }
        return render(request, 'tambah_barang.html', konteks)

def tambah_membership(request):
    if request.POST:
        form = FormMembership(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = FormMembership()
            konteks = {
                'form' : form,
            }
            return render(request, 'tambah_membership.html', konteks)
    else:

        form=FormMembership()
        konteks={
            'form':form,
        }
        return render(request, 'tambah_membership.html', konteks)

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request, 'tb_items.html', konteks)

def Membership_View(request):
    memberships=Membership.objects.all()

    konteks={
        'memberships':memberships,
    }
    return render(request, 'tb_members.html', konteks)

def ubah_brg(request, id_barang):
    barangs = Barang.objects.get(id = id_barang)
    if request.POST:
        form = FormBarang(request.POST, instance = barangs)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubah_brg', id_barang = id_barang)
    else:
        form = FormBarang(instance=barangs)
        konteks = {
            'form' : form,
            'barangs' : barangs
        }

        return render (request, 'ubah_brg.html', konteks)

def ubah_mem(request, id_member):
    memberships = Membership.objects.get(id = id_member)
    if request.POST:
        form = FormMembership(request.POST, instance = memberships)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubah_mem', id_member = id_member)
    else:
        form = FormMembership(instance=memberships)
        konteks = {
            'form' : form,
            'memberships' : memberships
        }

        return render (request, 'ubah_mem.html', konteks)

def hapus_brg(request, id_barang):
    barangs = Barang.objects.filter(id = id_barang)
    barangs.delete()
    
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }

    messages.success(request, "Data Terhapus")
    return render(request, 'tb_items.html', konteks)

def hapus_mem(request, id_member):
    memberships = Membership.objects.filter(id = id_member)
    memberships.delete()
    
    memberships=Membership.objects.all()

    konteks={
        'memberships':memberships,
    }

    messages.success(request, "Data Terhapus")
    return render(request, 'tb_members.html', konteks)