from collections import defaultdict

from rest_framework.decorators import api_view, renderer_classes
from django.utils import timezone
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from accounts.models import CustomUser

import psycopg2


def make_connection():
    hostname = 'localhost'
    database = 'paragraphs'
    username = 'postgres'
    pwd = "rosansen7"
    port_id = 5432

    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)

    return conn


# Create your views here.
@csrf_exempt
@api_view(["POST"])
@login_required
def post_paragraphs(request):

    data = request.data

    inputs = data.split("\r\n\r\n")
    for i in range(len(inputs)):
        inputs[i] = inputs[i].replace("\r\n", "")

    n_paras = len(inputs)

    conn = make_connection()
    cur = conn.cursor()
    insert_statement = "INSERT INTO newapp_paragraphs (para_id,para_text) VALUES (%s,%s)"
    for i in range(n_paras):
        cur.execute(insert_statement, (f"para{i + 1}", inputs[i]))

    conn.commit()

    insert_statement = "INSERT INTO newapp_wordmap (word,para_id) VALUES (%s,%s)"

    para_word_dict = defaultdict(set)
    for i in range(n_paras):
        splitted_text = inputs[i].lower()
        splitted_text = splitted_text.replace(",", " ")
        splitted_text = splitted_text.replace(".", " ")
        splitted_text = splitted_text.split()
        for word in splitted_text:

            if word not in para_word_dict:
                para_word_dict[word] = set()
                para_word_dict[word].add(f"para{i + 1}")
            else:
                para_word_dict[word].add(f"para{i + 1}")

    columns = para_word_dict.keys()
    for word in columns:
        for para_no in para_word_dict[word]:
            cur.execute(insert_statement, (word, para_no))
    conn.commit()
    cur.close()
    conn.close()
    return Response({
        'status': True,
        'message': "success paras entered to database"
    })
@csrf_exempt
@api_view(["GET"])
@login_required
def get_paras(request):
    word = str(request.data)
    word = word.lower()
    conn = make_connection()
    cur = conn.cursor()
    query = f"SELECT newapp_paragraphs.para_text FROM newapp_paragraphs INNER JOIN newapp_wordmap ON newapp_paragraphs.para_id = newapp_wordmap.para_id where newapp_wordmap.word = '{word}'"
    cur.execute(query)
    results = cur.fetchall()
    paras = ""
    count = 1
    for para in results:
        # paras += f"{count}."
        paras += para[0]
        # count += 1
        paras += "\n\n"

    cur.close()
    conn.close()
    return HttpResponse(paras, content_type='text/plain')


@csrf_exempt
def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not CustomUser.objects.filter(email=email).exists():
            return Response({
                'message': "User does not exist.Invalid username"
            })
        user = authenticate(email=email, password=password)
        if user is None:
            return Response({
                'message': "Invalid password"
            })
        else:
            login(request,user)
            return JsonResponse({'status':"Logged In"})
    else:
        return JsonResponse({
            'status': False,
            'message': "Invalid request"
        })

@csrf_exempt
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        new_email = request.POST.get("email")
        dob = request.POST.get("dob")
        password = request.POST.get("password")

        user = CustomUser.objects.create_user(
            email=new_email,
            name=name,
            dob=dob,
            password=password
        )
        return JsonResponse({
            'status': True,
            'message': "User succesfully registered"
        })

    return JsonResponse({
        'status': False,
        'message': "User already exists"
    })
