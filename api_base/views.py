from django.shortcuts import render


# My imports
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse , HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
import json



# Models Imports
from .models import Chercheur , Person , Article , Admin , Journal , Editeur , Message , Conversation

import requests

# Create your views here.


######################################################

@csrf_exempt
@api_view(['POST'])
def createMessage(request):
        

    data = json.loads(request.body)
    print("-------------------------------")
    print(data)
    print("-------------------------------")
    message = Message.objects.create(
        EmmetteurID = data['EmmetteurID'],
        RecepteurID = data['RecepteurID'],
        Conversation = data['Conversation'],
        Time = data['Time'],
        Contenu = data['Contenu'],
    )


    return JsonResponse({
        'EmmetteurID': message.EmmetteurID,
        'RecepteurID': message.RecepteurID,
        'Conversation': message.Conversation,
        'Time': message.Time,
        'Contenu': message.Contenu
    }, status=201)

######################################################

@csrf_exempt
@api_view(['POST'])
def getMessage(request):

    data = json.loads(request.body)
    messagesSent = Message.objects.filter(EmmetteurID=data['id'])
    messagesReceived = Message.objects.filter(RecepteurID=data['id'])

    messagesSent_data = []
    messagesReceived_data = []

    for message in messagesSent:
        messagesSent_data.append({
            "ID": message.ID,
            "EmmetteurID": message.EmmetteurID,
            "RecepteurID": message.RecepteurID,
            "Conversation": message.Conversation,
            "Time": message.Time,
            "Contenu": message.Contenu,
        })

    for message in messagesReceived:
        messagesReceived_data.append({
            "ID": message.ID,
            "EmmetteurID": message.EmmetteurID,
            "RecepteurID": message.RecepteurID,
            "Conversation": message.Conversation,
            "Time": message.Time,
            "Contenu": message.Contenu,
        })

    # print(data['id'])

    return JsonResponse({
        "Sent" : messagesSent_data ,
        "Received" : messagesReceived_data,
    }, safe=False, status=200)



######################################################

@csrf_exempt
@api_view(['POST'])
def createConversation(request):
        

    data = json.loads(request.body) 

    conversation = Conversation.objects.create(
        CreateurID = data['CreateurID'],
        Logo = data['Logo'],
    )


    return JsonResponse({
        'CreateurID': conversation.CreateurID,
        'Logo': conversation.Logo,
    }, status=201)

######################################################

@csrf_exempt
@api_view(['GET'])
def getAllUsers(request):
    # Get all Chercheur objects
    chercheurs = Chercheur.objects.all()

    # Create a list to store the Chercheur data
    chercheur_data = []

    # Loop through the Chercheur objects and append the data to the list
    for chercheur in chercheurs:
        chercheur_data.append({
            "ID": chercheur.person.ID,
            "Name": chercheur.person.Name,
            "Email": chercheur.person.Email,
            "Universite": chercheur.Universite,
            "Fonction": chercheur.Fonction
        })

    # Return the Chercheur data as a JSON response
    return JsonResponse(chercheur_data, safe=False, status=200)

###################################################################333

@csrf_exempt
@api_view(['GET', 'DELETE'])
def DeleteChercheurById(request, id):
    # try:
        # Fetch the Chercheur object with the given id
    chercheur = Chercheur.objects.get(person__ID=id)

        # if request.method == 'GET':
        #     # Prepare the response data
        #     chercheur_data = {
        #         "ID": chercheur.person.ID,
        #         "Name": chercheur.person.Name,
        #         "Email": chercheur.person.Email,
        #         "Universite": chercheur.Universite,
        #         "Fonction": chercheur.Fonction
        #     }

        #     return JsonResponse(chercheur_data, status=200)

        # elif request.method == 'DELETE':
        #     # Delete the Chercheur object
    chercheur.delete()
    return JsonResponse({
        "message": "Chercheur deleted successfully"
    }, status=204)

    # except Chercheur.DoesNotExist:
    #     return JsonResponse({
    #         "message": "Chercheur not found"
    #     }, status=404)

###################################################################333

@csrf_exempt
@api_view(['POST'])
def CheckUserCreds(request):
    data = json.loads(request.body)

    # Get the email and password from the request data
    email = data['Email']
    password = data['Password']

    # Check if the user exists in the Person model
    persons = Person.objects.filter(Email=email)

    if len(persons) == 1:
        person = persons[0]
        # Verify the password
        if person.Password == password:
            # The user is valid, so we can return a successful response
            return JsonResponse({
                'message': 'User authenticated successfully',
                'user': {
                    'id': person.ID,
                    'name': person.Name,
                    'email': person.Email
                }
            }, status=200)
        else:
            # The password is invalid, so return an error response
            return JsonResponse({
                'message': 'Invalid email or password'
            }, status=401)
    elif len(persons) == 0:
        # The user doesn't exist, so return an error response
        return JsonResponse({
            'message': 'Invalid email or password'
        }, status=401)
    else:
        # There are multiple users with the same email, this is an error
        return JsonResponse({
            'message': 'Multiple users with the same email found'
        }, status=500)
    


######################################################

@csrf_exempt
@api_view(['POST'])
def CheckAdminCreds(request):
    data = json.loads(request.body)

    # Get the email and password from the request data
    email = data['Email']
    password = data['Password']

    # Check if the user exists in the Person model
    persons = Admin.objects.filter(Email=email)

    if len(persons) == 1:
        person = persons[0]
        # Verify the password
        if person.Password == password:
            # The user is valid, so we can return a successful response
            return JsonResponse({
                'message': 'User authenticated successfully',
                'user': {
                    'id': person.ID,
                    'name': person.Name,
                    'email': person.Email
                }
            }, status=200)
        else:
            # The password is invalid, so return an error response
            return JsonResponse({
                'message': 'Invalid email or password'
            }, status=401)
    elif len(persons) == 0:
        # The user doesn't exist, so return an error response
        return JsonResponse({
            'message': 'Invalid email or password'
        }, status=401)
    else:
        # There are multiple users with the same email, this is an error
        return JsonResponse({
            'message': 'Multiple users with the same email found'
        }, status=500)
    
######################################################

@csrf_exempt
@api_view(['POST'])
def CheckEditorCreds(request):
    data = json.loads(request.body)

    # Get the email and password from the request data
    email = data['Email']
    password = data['Password']

    # Check if the user exists in the Editeur model
    try:
        editor = Editeur.objects.get(person__Email=email)
        # Verify the password
        if editor.person.Password == password:
            # The user is valid, so we can return a successful response
            return JsonResponse({
                'message': 'User authenticated successfully',
                'user': {
                    'id': editor.person.ID,
                    'name': editor.person.Name,
                    'email': editor.person.Email
                }
            }, status=200)
        else:
            # The password is invalid, so return an error response
            return JsonResponse({
                'message': 'Invalid email or password'
            }, status=401)
    except Editeur.DoesNotExist:
        # The user doesn't exist, so return an error response
        return JsonResponse({
            'message': 'Invalid email or password'
        }, status=401)


######################################################

@csrf_exempt
@api_view(['POST'])
def createEditor(request):
        

    data = json.loads(request.body) 

    person = Person.objects.create(
        Name=data['Name'],
        Email=data['Email'],
        Password=data['Password']
    )

    editeur = Editeur.objects.create(
        person=person,
        Thematique=data['Thematique']
    )

    return JsonResponse({
        'Name': editeur.person.Name,
        'Thematique': editeur.Thematique,
        'Email': editeur.person.Email,
        'Password': editeur.person.Password
    }, status=201)

######################################################

@csrf_exempt
@api_view(['POST'])
def createChercheur(request):
    data = json.loads(request.body)

    email = data['Email']
    persons = Person.objects.filter(Email=email)

    if not persons.exists():
        person = Person.objects.create(
            Name=data['Name'],
            Email=data['Email'],
            Password=data['Password']
        )

        chercheur = Chercheur.objects.create(
            person=person,
            Universite=data['Universite'],
            Fonction=data['Fonction'],
        )

        return JsonResponse({
            'Name': chercheur.person.Name,
            'Universite': chercheur.Universite,
            'Fonction': chercheur.Fonction,
            'Email': chercheur.person.Email,
            'Password': chercheur.person.Password
        }, status=201)
    else:
        return JsonResponse({
            'message': 'Email is already used'
        }, status=500)

######################################################


@csrf_exempt
@api_view(['POST'])
def createArticle(request):

    data = json.loads(request.body)

    article = Article.objects.create(
        Name=data['Name'],
        Link=data['Link'],
        Image=data['Image'],
        Theme=data['Theme'],
        JournalID=data['JournalID'],
        PersonID=data['PersonID'],
        Status=data['Status'],
    )
    return JsonResponse({
        "Name" : article.Name,
        "Link" : article.Link,
        "Image" : article.Image,
        "Theme" : article.Theme,
        "JournalID" : article.JournalID,
        "PersonID" : article.PersonID,
        "Status" : article.Status,
        }, status=201)


######################################################


@csrf_exempt
@api_view(['POST'])
def getArticle(request):

    data = json.loads(request.body)
    articles = Article.objects.filter(PersonID=data['id'])

    article_data = []
    for article in articles:
        article_data.append({
            "Ref": article.Ref,
            "Name": article.Name,
            "Link": article.Link,
            "Image": article.Image,
            "Theme": article.Theme,
            "JournalID": article.JournalID,
            "PersonID": article.PersonID,
            "Status" : article.Status,
        })

    print(data['id'])

    return JsonResponse(article_data, safe=False, status=200)

#####################################################

@csrf_exempt
@api_view(['GET'])
def getArticlebySearch(request, search_term):

    # data = json.loads(request.body)
    articles = Article.objects.filter(Name__icontains=search_term)
    # articles = Article.objects.filter(PersonID=data['id'])

    article_data = []
    for article in articles:
        article_data.append({
            "Ref": article.Ref,
            "Name": article.Name,
            "Link": article.Link,
            "Image": article.Image,
            "Theme": article.Theme,
            "JournalID": article.JournalID,
            "PersonID": article.PersonID,
            "Status" : article.Status,
        })

    # print(data['id']) 

    return JsonResponse(article_data, safe=False, status=200)

######################################################

@csrf_exempt
@api_view(['POST'])
def Approuvearticle(request):
    data = json.loads(request.body)
    article = Article.objects.get(Ref=data['Ref'])
    article.Status = 'Approved'
    article.save()
    return Response({'message': 'Article approved successfully.'}, status=200)

######################################################

@csrf_exempt
@api_view(['POST'])
def DeleteArticle(request):
    data = json.loads(request.body)
    article = Article.objects.get(Ref=data['Ref'])
    article.delete()
    return Response({'message': 'Article deleted successfully.'}, status=200)

######################################################

@csrf_exempt
@api_view(['GET'])
def getNotApprovedArticles(request):

    articles = Article.objects.filter(Status='NApproved')

    article_data = []

    for article in articles:
        article_data.append({
            "Ref": article.Ref,
            "Name": article.Name,
            "Link": article.Link,
            "Image": article.Image,
            "Theme": article.Theme,
            "JournalID": article.JournalID,
            "PersonID": article.PersonID,
            "Status" : article.Status,
        })

    return JsonResponse(article_data, safe=False, status=200)

######################################################

@csrf_exempt
@api_view(['POST'])
def createJournal(request):

    data = json.loads(request.body)

    journal = Journal.objects.create(
        JournalID=data['JournalID'],
        Name=data['Name'],
        Link=data['Link'],
        Image=data['Image'],
    )
    return JsonResponse({
        "JournalID" : journal.JournalID,
        "Name" : journal.Name,
        "Link" : journal.Link,
        "Image" : journal.Image,
        }, status=201)

######################################################

@csrf_exempt
@api_view(['POST'])
def getJournal(request):

    data = json.loads(request.body)
    journals = Journal.objects.filter(PersonID=data['id'])

    article_data = []
    for journal in journals:
        article_data.append({
            "JournalID": journal.JournalID,
            "Name": journal.Name,
            "Link": journal.Link,
            "Image": journal.Image,
        })

    print(data['id'])

    return JsonResponse(article_data, safe=False, status=200)

######################################################

@csrf_exempt
@api_view(['GET'])
def getJournalALL(request):
    journals = Journal.objects.all()

    article_data = []
    for journal in journals:
        article_data.append({
            "JournalID": journal.JournalID,
            "Name": journal.Name,
            "Link": journal.Link,
            "Image": journal.Image,
        })

    return JsonResponse(article_data, safe=False, status=200)

########################################################

@csrf_exempt
@api_view(['GET'])
def getStats(request):

    ChercheurCnt= Chercheur.objects.count()
    EditeurCnt= Editeur.objects.count()
    ArticleCnt= Article.objects.count()
    JournalCnt= Journal.objects.count()

    stats_data = {
        'Researchers': ChercheurCnt,
        'Editors': EditeurCnt,
        'Articles': ArticleCnt,
        'Journals': JournalCnt
    }

    return JsonResponse(stats_data, safe=False, status=200)

