import copy

from django.core.paginator import Paginator
from django.shortcuts import render

QUESTIONS = [
    {
        'title': f'Title {i}',
        'id': i,
        'text': f'This is text for question # {i}'
    } for i in range(30)
]

ANSWERS = [
    {
        'title': f'Title {j}',
        'id': j,
        'text': f'This is text for answer # {j}'
    } for j in range(10)
]


def index(request):
    if request.GET.get('page'):
        page_num = int(request.GET.get('page'))
    else:
        page_num = 1
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)
    return render(
        request, 'index.html',
        context={'questions': page.object_list, 'page_obj': page}

    )


def index_auth(request):
    if request.GET.get('page'):
        page_num = int(request.GET.get('page'))
    else:
        page_num = 1
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)
    return render(
        request, 'index_auth.html',
        context={'questions': page.object_list, 'page_obj': page}
    )


def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    if request.GET.get('page'):
        page_num = int(request.GET.get('page'))
    else:
        page_num = 1
    paginator = Paginator(hot_questions, 5)
    page = paginator.page(page_num)
    return render(
        request, 'hot.html',
        context={'questions': page.object_list, 'page_obj': page}
    )

def hot_auth(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    if request.GET.get('page'):
        page_num = int(request.GET.get('page'))
    else:
        page_num = 1
    paginator = Paginator(hot_questions, 5)
    page = paginator.page(page_num)
    return render(
        request, 'hot_auth.html',
        context={'questions': page.object_list, 'page_obj': page}
    )


def question(request, question_id):
    one_question = QUESTIONS[question_id]
    return render(
        request, 'one_question.html',
        context={'question': one_question}
    )

def answer(request, answer_id):
    one_answer = ANSWERS[answer_id]
    return render(
        request, 'one_question.html',
        context={'answer': one_answer}
    )


def question_auth(request, question_id):
    one_question = QUESTIONS[question_id]
    return render(
        request, 'one_question_auth.html',
        context={'question': one_question}
    )


def bender(request):
    if request.GET.get('page'):
        page_num = int(request.GET.get('page'))
    else:
        page_num = 1
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)
    return render(
        request, 'bender.html',
        context={'questions': page.object_list, 'page_obj': page}
    )

def bender_auth(request):
    if request.GET.get('page'):
        page_num = int(request.GET.get('page'))
    else:
        page_num = 1
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)
    return render(
        request, 'bender_auth.html',
        context={'questions': page.object_list, 'page_obj': page}
    )


def black_jack(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    if request.GET.get('page'):
        page_num = int(request.GET.get('page'))
    else:
        page_num = 1
    paginator = Paginator(hot_questions, 5)
    page = paginator.page(page_num)
    return render(
        request, 'black_jack.html',
        context={'questions': page.object_list, 'page_obj': page}
    )

def black_jack_auth(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    if request.GET.get('page'):
        page_num = int(request.GET.get('page'))
    else:
        page_num = 1
    paginator = Paginator(hot_questions, 5)
    page = paginator.page(page_num)
    return render(
        request, 'black_jack_auth.html',
        context={'questions': page.object_list, 'page_obj': page}
    )


def user_settings(request):
    return render(
        request, 'user_settings.html',
    )


def user_login(request):
    return render(
        request, 'user_login.html',
    )


def sign_up(request):
    return render(
        request, 'sign_up.html',
    )

def ask(request):
    return render(
        request, 'ask.html',
    )

