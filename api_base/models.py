from django.db import models

# Create your models here.

class Person(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)

    # ! Creds
    Email = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return self.ID


#####################################################################    
    

class Chercheur(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='chercheur'
    )
    Universite = models.CharField(max_length=40)
    Fonction = models.CharField(max_length=40)

    def VoirMesArticle(self):
        print("voirMesArticle()")

    def AjouterunArticle(self):
        print("voirMesArticle()")


#####################################################################    
    

class Admin(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='admin'
    )
    Departement = models.CharField(max_length=40)
    Fonction = models.CharField(max_length=40)

######################################################################

  

class Editeur(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='editeur'
    )
    Thematique = models.CharField(max_length=40)






#####################################################################

class Article(models.Model):
    Ref = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=40)
    Link = models.CharField(max_length=40)
    Image = models.CharField(max_length=400)
    Theme = models.CharField(max_length=40)
    JournalID = models.CharField(max_length=40)
    Theme = models.CharField(max_length=40)
    PersonID = models.CharField(max_length=40)
    Status = models.CharField(max_length=40)


#####################################################################

class Journal(models.Model):
    JournalID = models.CharField(max_length=40)
    Name = models.CharField(max_length=40)
    Link = models.CharField(max_length=40)
    Image = models.CharField(max_length=400)


#####################################################################

class Message(models.Model):
    ID = models.AutoField(primary_key=True)
    EmmetteurID = models.CharField(max_length=40)
    RecepteurID = models.CharField(max_length=40)
    Conversation = models.CharField(max_length=40)
    Time = models.CharField(max_length=40)
    Contenu = models.CharField(max_length=400)
    


class Conversation(models.Model):
    ID = models.AutoField(primary_key=True)
    CreateurID = models.CharField(max_length=40)
    Logo = models.CharField(max_length=40)
    
#####################################################################

# class PersonCred(models.Model):
#     Email = models.CharField(max_length=30)
#     Password = models.CharField(max_length=30)

#     def __str__(self):
#         return self.Email

#####################################################################


# class Editeur(models.Model):
#     person = models.OneToOneField(
#         Person,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name='editeur'
#     )
#     Thematique = models.CharField(max_length=40)

#     def ConfirmerUnArticle(self):
#         print("voirMesArticle()")


#####################################################################


# class Admin(models.Model):
#     person = models.OneToOneField(
#         Person,
#         on_delete=models.CASCADE,
#         primary_key=True,
#         related_name='admin'
#     )
#     Departement = models.CharField(max_length=40)
#     Fonction = models.CharField(max_length=40)

