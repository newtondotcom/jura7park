from django.contrib import admin
from db.models import Stock, repenigmes, codeqr, points, Photo, paris, histodinos, events, Enigme, Produit, achats

@admin.register(achats)
class AchatsAdmin(admin.ModelAdmin):
    list_display = ('produit', 'user','date', 'prix')

@admin.register(Produit)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'stock')
    ordering = ('price',)

@admin.register(Enigme)
class EnigmeAdmin(admin.ModelAdmin):
    list_display = ('numero_enigme', 'reponse', 'user', 'date', 'is_valid')
    list_filter = ('numero_enigme', 'reponse', 'user', 'date', 'is_valid')
    search_fields = ('numero_enigme', 'reponse', 'user', 'date', 'is_valid')
    ordering = ('numero_enigme', 'reponse', 'user', 'date', 'is_valid')

@admin.register(events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['jour','periode','horaires','nom']
    ordering = ('jour','periode','horaires','nom')


@admin.register(histodinos)
class histodinosAdmin(admin.ModelAdmin):
    list_display = ['defi', 'beneficaire', 'montant', 'payeur','date']
    list_filter = ['defi', 'beneficaire', 'montant', 'payeur','date']
    search_fields = ['defi', 'beneficaire', 'montant', 'payeur','date']
    ordering = ['defi', 'beneficaire', 'montant', 'payeur','date']

@admin.register(paris)
class parisAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'mise', 'gagnant','is_paid','numero')
    list_filter = ('user', 'date', 'mise', 'gagnant','numero')
    search_fields = ('user', 'date', 'mise', 'gagnant','numero')
    ordering = ('user', 'date', 'mise', 'gagnant','numero')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('jour', 'legende', 'lien')
    ordering = ('jour',)

@admin.register(points)
class PointsAdmin(admin.ModelAdmin):
    list_display = ('surnom', 'point', 'avatar')
    list_filter = ('surnom',)
    search_fields = ('surnom',)

@admin.register(codeqr)
class CodeQrAdmin(admin.ModelAdmin):
    list_display = ('title', 'datecreation', 'dateutil', 'createur', 'utilisateur', 'points', 'utilise', 'code','nb_utilisation')
    list_filter=('utilise','dateutil', 'datecreation','nb_utilisation')
    ordering = ('points',)

@admin.register(repenigmes)
class repenigmesAdmin(admin.ModelAdmin):
    list_display = ('numero_enigme', 'reponse')
    list_filter = ('numero_enigme', 'reponse')
    search_fields = ('numero_enigme', 'reponse')
    ordering = ('numero_enigme', 'reponse')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('surnom', 'avatar', 'nomavatar', 'date')
    list_filter = ('surnom', 'avatar', 'nomavatar', 'date')
    search_fields = ('surnom', 'avatar', 'nomavatar', 'date')
    ordering = ('surnom', 'avatar', 'nomavatar', 'date')
