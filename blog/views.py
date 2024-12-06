from django.shortcuts import render, redirect
from .models import Post, Comment, Contact
import requests
from .paginator import Pagination
from django.conf import settings

def home_view(request):
    posts = Post.objects.filter(is_published=True)
    d = {
        'posts': posts
    }
    return render(request, 'index.html', context=d)

def articles_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    # another option ->
    # posts = sorted(posts, key=lambda post: post.created_at, reverse=True)
    # pagination
    data = request.GET
    page_number = int(data.get('page', 1))
    paginator = Pagination(posts,2)

    d = {
        'posts': paginator.get_page(page_number),
        'page_range': range(1, paginator.page_count + 1),
        'current_page': page_number,
        'next_page': page_number + 1,
        'previous_page': page_number -1,
        'is_last': paginator.is_last(page_number),
        'is_first': paginator.is_first(page_number)
    }

    return render(request, 'blog.html', context=d)

def article_detail_view(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)

    d = {
        'post': post,
        'comments': comments,
    }

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        website = data.get('website')
        message = data.get('message')
        obj = Comment.objects.create(post = post, name = name, email = email, website = website, message = message)
        obj.save()
        return redirect(f'/articles/{pk}')

    return render(request, 'blog-single.html',  context=d)

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('full_name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        obj = Contact.objects.create(full_name = name, email = email, subject = subject, message = message)
        obj.save()
        res = requests.get(settings.BASE_URL.format(settings.TELEGRAM_BOT_TOKEN, settings.TELEGRAM_CHANNEL_ID,
                                            f'name: {name} \nemail: {email} \nsubject: {subject} \nmessage:{message}'))
        print(res)
        return redirect('/contact')

    return render(request, 'contact.html')

def category_view(request, category_name):
    posts = Post.objects.filter(category__name = category_name)

    data = request.GET
    page_number = int(data.get('page', 1))
    paginator = Pagination(posts, 1)
    print(paginator)
    d = {
        'posts': paginator.get_page(page_number),
        'cat_name': category_name,
        'page_range': range(1, paginator.page_count + 1),
        'current_page': page_number,
        'next_page': page_number + 1,
        'previous_page': page_number - 1,
        'is_last': paginator.is_last(page_number),
        'is_first': paginator.is_first(page_number)
    }
    return render(request, 'category.html', context=d)