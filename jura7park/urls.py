from django.contrib import admin
import jura7park.views as views
from django.urls import path, include

urlpatterns = [
    path('ping', views.ping, name='ping'),
    path('shop/<nb>', views.shop),
    path('ld',views.leaderboard),
    path('enigmes',views.enigmelist),
    path('enigme/<nb>',views.enigme),
    path('repenigme',views.repenigme),
    path('registerbet/<id>',views.registerbet),
    path('bet',views.tempo),
    path('revealdino',views.revealdino),
    path('remerciements', views.remerciements),
    ##admin panel
    path('admin/', admin.site.urls),
    #path('api',include(router.urls)),
    path('photos', views.showphotos),
    ##where an admin can create a code qr
    path('createcodeqr',views.createcodeqr),
    ##where an admin shows the code qr created
    path('codeqrcreated',views.codeqrcreated),
    ##where a user can validate a buying
    path('validate/<name>',views.validate),
    ##where a user sees that is buying is confirmed
    path('validatedbuying/<name2>',views.validatedbuying),
    ##where a user validates a code
    path('validateqrcode/<name>',views.validateqrcode),
    ##where a user sees that is qrcode is confirmed
    path('validatedqrcode/<name2>',views.validatedqrcode),
    ##my account page
    path('myaccount',views.my_account),

    ##Where to register an user as a staff
    path('registerstaff/<name>',views.registerstaff),
    ##Where to register an user as a admin
    path('registeradmin/<name>',views.registeradmin),
    ##Where to unregister an user as a staff
    path('unregisterstaff/<name>',views.unregisterstaff),
    ##Show the page nb of saved avatars
    path('avatarlist/<nb>',views.genavatarlist),
    ##Define the current avatar
    path('chooseavatar/<nb>',views.chooseavatar),
    ##Reset balance
    path('resetbalance',views.resetbalance),
    ##Update the balance of the user blaze with the value points for the reason defi
    path('ub/<blaze>/<points>/<defi>',views.ub),
    ##Adjust the balance of the user blaze with the value points for the reason raison
    path('adjust/<blaze>/<points>/<raison>',views.adjust),
    ##Shows the buying list
    path('achats',views.achats),
    ##Shows the qrcode list
    path('codes',views.codes),
    ##Shows the qrcode list
    path('defis',views.defis),
    ##Pay Monday Bet
    path('paylundi',views.paylundi),
    ##Pay users for bet n1
    path('paybet1/<winner>/<cote>',views.paybet1),
    ##Pay users for bet n2
    path('paybet2/<winner>/<cote>',views.paybet2),

    ###Notifications
    path('webpush/', include('webpush.urls')),
    path('testnotif', views.testnotif),
    path('sendnotif', views.sendnotif),
    #path('sw.js', TemplateView.as_view(template_name='slistener.js', content_type='application/x-javascript')),

    ###PWA
    path('offline', views.offline),

    ###MUST BE AT THE END
    path('', include('pwa.urls')),

]

admin.site.site_header  =  "Jura7Park"
admin.site.site_title  =  "Jura7Park Admin"
admin.site.index_title  =  "Welcome to Jura7Park Admin"
