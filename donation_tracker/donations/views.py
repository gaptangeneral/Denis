from django.shortcuts import render, redirect
from .models import Donation
from .forms import DonationForm

def donation_list(request):
    if request.method == 'POST':
        form = DonationForm(request.POST) # Gönderilen verilerle formu doldur
        if form.is_valid(): # Form geçerli mi kontrol et
            form.save() # Form geçerliyse veritabanına kaydet
            return redirect('donations:donation_list') # Başarılı kayıttan sonra sayfayı yenile (formun temizlenmesi için)
        # Form geçerli değilse, hatalarla birlikte form tekrar şablona gönderilecek (aşağıdaki render ile)
    else:
        form = DonationForm() # GET isteği için boş form oluştur

    donations = Donation.objects.all().order_by('-created_at')
    context = {
        'donations': donations,
        'form': form, # Formu şablona gönder
    }
    return render(request, 'donations/index.html', context)

def add_donation(request):
    # Şimdilik sadece basit bir sayfa gösterelim veya ana sayfaya yönlendirelim.
    # Formu ve kaydetme mantığını bir sonraki adımda ekleyeceğiz.
    # Örneğin, geçici olarak ana sayfaya yönlendirebiliriz:
    # return redirect('donations:donation_list')
    # Veya boş bir template render edebiliriz (henüz oluşturmadık):
    return render(request, 'donations/add_donation.html') # add_donation.html adında bir şablon oluşturmamız gerekecek