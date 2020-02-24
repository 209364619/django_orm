from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from myform.models import UserForm
from django.views.decorators.http import require_POST
from django.views import View
# Create your views here.

@require_POST
def form_test(request):
    user_form = UserForm(request.POST)
    if user_form.is_valid():
        print(user_form)
        # print(user_form.age)
        return HttpResponse('username:{} age:{}'.format(user_form.name, user_form.age))
    else:
        return HttpResponse('form is invalid!')

def  fun_views(request):
    '''
    基于函数视图
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return HttpResponse('function views: get method')
    elif request.method == 'POST':
        return HttpResponse('function views: post method')
    elif request.method == 'DELETE':
        return HttpResponse('function views: delete method')
    else:
        return HttpResponse('the method is not defined!')

class ClassViews(View):
    def get(self, request):
        return HttpResponse('class views: get method')
    def post(self, request):
        return HttpResponse('class views: post method')
    def delete(self, request):
        return HttpResponse('class views: delete method')