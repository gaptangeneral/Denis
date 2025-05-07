from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'amount', 'donation_status', 'created_at', 'phone_number') # Listede görünecek alanlar
    list_filter = ('donation_status', 'created_at') # Filtreleme seçenekleri
    search_fields = ('name_surname', 'phone_number', 'explanation') # Arama yapılabilecek alanlar
    list_editable = ('donation_status',) # Listeden direkt düzenlenebilecek alanlar

admin.site.register(Donation, DonationAdmin)