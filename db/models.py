from django.db import models

class Produit(models.Model):
    title = models.CharField(max_length=100,primary_key=False)
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True,primary_key=False)
    image = models.ImageField(upload_to='')
    stock = models.IntegerField(null=True, blank=True,primary_key=False)

    def __str__(self):
        return self.title

class achats(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    prix = models.IntegerField(null=True, blank=True,primary_key=False)

class Enigme(models.Model):
    numero_enigme = models.IntegerField()
    reponse = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=False)

class events(models.Model):
    time_choices =(
        ('1','Matin'),
        ('2','Midi'),
        ('3','Aprem'),
        ('4','Soir')
    )
    day_CHOICES = (
        ('1', 'Lundi'),
        ('2', 'Mardi'),
        ('3', 'Mercredi'),
        ('4', 'Jeudi'),
        ('5', 'Vendredi'),
        ('6', 'Samedi'),
        ('7', 'Dimanche'),
    )
    jour= models.CharField(choices=day_CHOICES,max_length=1)
    periode=models.CharField(choices=time_choices,max_length=1)
    horaires = models.TextField()
    nom = models.TextField()

day_CHOICES = (
    ('1', 'Rembobiner'),
    ('2', 'Jura7Staff'),
    ('3', 'Dans la peau d\'un dino'),
    ('4', 'Eruption'),
    ('5', 'Clean my house'),
    ('6', 'Dompteur de dinos'),
    ('7', 'Instagraaaow'),
    ('8', 'Pro jura7'),
    ('9', 'Cruta7'),
    ('10', 'Herbivore confirmé'),
    ('11', 'Fictif'),
    ('12', 'Indiana Jaune'),
    ('13', 'Photosaure'),
    ('14', 'Jura-N7'),
    ('15', 'Camouflage'),
    ('16', 'Le cri d\'amour'),
    ('17', 'Les Dinoms'),
    ('18', 'Dino Train'),
    ('19', 'Dino di Caprio'),
    ('20', 'Cringeausaure'),
    ('21', 'Dinorigolo'),
    ('22', 'Photodino'),
    ('23', 'Cri au dino'),
    ('24', 'Surviva7'),
    ('25', 'Sa place est dans le musée'),
    ('26', 'Participation Rallye Colloc'),
    )

# Create your models here.
class histodinos(models.Model):
    defi = models.CharField(choices=day_CHOICES,max_length=2)
    beneficaire = models.ForeignKey('auth.User', related_name='benf',on_delete=models.CASCADE)
    montant = models.IntegerField()
    payeur = models.ForeignKey('auth.User', related_name='pay',on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)

    def get_day_display(self):
        return dict(day_CHOICES)[self.defi]

class paris(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    mise = models.IntegerField()
    gagnant = models.IntegerField()
    numero = models.IntegerField(null = True, blank = True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Photo(models.Model):
    MY_CHOICES = (
        ('6', 'Samedi'),
        ('7', 'Dimanche'),
        ('1', 'Lundi'),
        ('2', 'Mardi'),
        ('3', 'Mercredi'),
        ('4', 'Jeudi'),
        ('5', 'Vendredi'),
    )
    jour = models.CharField(max_length=1, choices=MY_CHOICES)
    legende = models.CharField(max_length=500)
    lien = models.CharField(max_length=500)

class points(models.Model):
    #surnom = models.CharField(max_length=100)
    surnom = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    point = models.IntegerField()
    avatar = models.TextField()
    nomavatar = models.TextField(null=True, blank=True)

class codeqr(models.Model):
    title = models.CharField(max_length=100)
    datecreation = models.DateTimeField(auto_now_add=True)
    dateutil = models.DateTimeField(null=True, blank=True)
    createur = models.ForeignKey('auth.User', related_name='creat_codeqr', on_delete=models.CASCADE)
    utilisateur = models.ForeignKey('auth.User', related_name='user_codeqr', on_delete=models.CASCADE, null=True, blank=True)
    points = models.IntegerField()
    utilise = models.BooleanField()
    code=models.CharField(max_length=100,null=True, blank=True)
    nb_utilisation = models.IntegerField(default=1)
    lien = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.title

class repenigmes(models.Model):
    day_CHOICES = (
        ('3', 'Lundi'),
        ('4', 'Mardi'),
        ('5', 'Mercredi'),
        ('6', 'Jeudi'),
        ('7', 'Vendredi'),
        ('1', 'Samedi'),
        ('2', 'Dimanche'),
    )
    numero_enigme = models.CharField(choices=day_CHOICES,max_length=1)
    reponse = models.CharField(max_length=200)
    indice = models.TextField(null=True,blank=True)



class Stock(models.Model):
    surnom = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    avatar = models.TextField()
    nomavatar = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
