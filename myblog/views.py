from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Contact_info, subscribe, blog_post,comments
from .forms import Blog_Form, BlogPost_Form,CommentForm
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

@login_required(login_url="loginuser")
def home(request):
    # Fetch the data from db
    x = Category.objects.all()
    print(x)

    if request.method == 'GET':
        return render(request, 'myblog/home.html', {"category": x})
    elif request.method == 'POST':
        email = request.POST.get('s_email')

        # Check if the email already exists
        existing_subscription = subscribe.objects.filter(sub_email=email).exists()

        if not existing_subscription:
            # If the email doesn't exist, create a new subscription
            new_subscription = subscribe(sub_email=email)
            new_subscription.save()
            return render(request, 'myblog/home.html', {'feedback': 'Your message has been recorded', "category": x})
        
        # If the email already exists, display a message
        return render(request, 'myblog/home.html', {'feedback': 'This email is already subscribed', "category": x})
    



def contact(request):
    #return HttpResponse('<h1>this is the contact page</h1>')
    if request.method == 'GET':
        return render(request, 'myblog/contact.html')
    elif request.method == 'POST':
        name = request.POST.get('name1')
        email = request.POST.get('email1')
        message = request.POST.get('message1')
        x = Contact_info(u_name=name , u_email=email , u_message=message)
        x.save()
        return render(request,'myblog/contact.html',{'feedback':'Your message has been recorded'})
    


        
def ck(request):
    x = BlogPost_Form()
    return render(request,'myblog/ck.html',{"x":x})




def blog_details(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    print(obj)
    print(blog_id)
    z=obj.view_count
    z=z+1
    obj.view_count=z
    obj.save()
    comments_list = comments.objects.filter(blog=obj).order_by('-created_at')
    return render(request,'myblog/blog_details.html', {"obj":obj, 'comments_list': comments_list})
    # return HttpResponse('blog_details')

def loginuser(request):
    if request.method == "GET":
        return render(request,'myblog/loginuser.html' , {'form' : AuthenticationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user= authenticate(request,username=a, password=b)
        if user is None:
            return render(request,'myblog/loginuser.html' , {'form' : AuthenticationForm() , 'error' : 'Invalid Credentials'})
        else:
            login(request,user)
            return redirect('home')
    
def signupuser(request):
    if request.method == "GET":
        return render(request,'myblog/signupuser.html' , {'form' : UserCreationForm()})
    else :
        a = request.POST.get('username')
        b = request.POST.get('password1') 
        c = request.POST.get('password2')   

        if b==c:
            if (User.objects.filter(username = a)):
                return render(request,'myblog/signupuser.html',{'form' : UserCreationForm(), 'error' : 'username already exists, try another username'})
            else:
                user = User.objects.create_user(username = a, password = b)
                user.save()
                login(request,user)
                return redirect('home')

        else:
            return render(request,'myblog/signupuser.html', {'form' : UserCreationForm(), 'error': 'password mismatched, try again'})

    
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')
    

    
def allblogs(request):
    page_number = request.GET.get("page")
    y = blog_post.objects.all()
    p = Paginator(y, 3)
    page_obj = p.get_page(page_number)
    return render(request,'myblog/allblogs.html',{"y":page_obj})


def blog(request):
    x = Blog_Form()  
    if request.method == "GET":
        return render(request,'myblog/blog.html',{"x":x})
    else:
        form = Blog_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'myblog/blog.html',{"x":x})
        

def blogfilter(request):
    # Extract the category from the request parameters
    category_name = request.GET.get('category')

    # If a category is provided, filter blog posts by that category, otherwise, get all blog posts
    if category_name:
        blogs = blog_post.objects.filter(blogcat__blog_cat=category_name)
    else:
        blogs = blog_post.objects.all()

    return render(request, 'myblog/blogfilter.html', {"blogs": blogs, "category": category_name})

def findproduct(request):
    if request.method == "POST":
        x = request.POST.get('prod_search')
        # print(x)
        mydata = Category.objects.filter(Q(blog_cat__icontains = x) | Q(blogcat_description__icontains = x))
        # print(mydata)
        if mydata:
            return render(request, 'myblog/home.html', {"category": mydata})
        else:
            return render(request, 'myblog/home.html', {"warning": 'No such item can be found among the blogs'})
    
def add_like(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    print (obj.like_count)
    y=obj.like_count
    y=y+1
    obj.like_count=y
    obj.save()
    return redirect('blog_details', obj.id)

def _comments(request,blog_id):
        com = request.POST.get('comment1')
        print(com)
        x = comments(u_comment=com, blog_id=blog_id)
        x.save()

        return redirect('/blog_details/'+blog_id)

def edit_comment(request, comment_id):
    comment = get_object_or_404(comments, id=comment_id)

    if request.method == 'POST':
        comment.u_comment = request.POST.get('edited_comment')
        comment.save()
        return redirect('blog_details', blog_id=comment.blog_id)

    context = {
        'comment': comment,
    }

    return render(request, 'myblog/edit_comment.html', context)



def delete_comment(request, comment_id):
    comment = get_object_or_404(comments, pk=comment_id)
    blog_id = comment.blog.id
    comment.delete()
    return redirect('blog_details', blog_id=blog_id)
        

