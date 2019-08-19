from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    create_table_for_home(request)
    return render(request,'courses_application/index.html')

def add_course(request):
    if request.method=="POST":
        errors = Course.objects.basic_validator(request.POST)

        if len(errors) > 0:

            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        
        else:
            new_entry = Course.objects.create(title=request.POST['title'], description=request.POST['description'])
            new_entry.save()

    return redirect('/')

def display_delete(request, course_id):
    context = {
            'course' : Course.objects.get(id=course_id),
        }

    return render(request,'courses_application/display_delete.html',context)

def process_delete(request, course_id):
    current_course = Course.objects.get(id=course_id)
    current_course.delete()

    return redirect ('/')

def comments(request, course_id):
    current_course = Course.objects.get(id=course_id)

    context = {
        'course' : current_course,
        'comments' : Comment.objects.filter(course=Course.objects.get(id=course_id))
    }

    return render(request,'courses_application/comments.html', context)

def process_comments(request, course_id):
    if request.method=="POST":
        errors = Comment.objects.basic_validator(request.POST)

        if len(errors) > 0:

            for key, value in errors.items():
                messages.error(request,value)
            return redirect(f'/courses/comments/{course_id}')
        
        else:
            current_course = Course.objects.get(id=course_id)
            new_entry = Comment.objects.create(username=request.POST['username'], comment=request.POST['comment'], course = current_course)
            new_entry.save()

            return redirect(f'/courses/comments/{course_id}')

def create_table_for_home(request):
    request.session['for_print'] = []
    courses = Course.objects.all()

    for x in range(0,len(courses),1):
        delete_url = f"<a href='/courses/destroy/{courses[x].id}' class='btn btn-sm btn-info'>Remove</a>"
        comments_url = f"<a href='/courses/comments/{courses[x].id}' class='btn btn-sm btn-info'>Comment</a>"
        request.session['for_print'].append(f"<tr><th scope='col'>{courses[x].id}</th><th scope='col'>{courses[x].title}</th><th scope='col'>{courses[x].description}</th><th scope='col'>{courses[x].created_at}</th><th scope='col'>{comments_url}</th><th scope='col'>{delete_url}</th></tr>")

    return redirect('/')