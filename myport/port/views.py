from django.shortcuts import render
from port.models import category, Article , Resume, Blog, Yourself

# Create your views here.
def home(request):
    contexts = Yourself.objects.all()
    resumes=Resume.objects.all()
    names = [context.name for context in contexts]
    aboutyou = [[context.about_you for context in contexts]]
    context ={'name': names , 'aboutyou': aboutyou, 'resume':resumes}
    return render(request,'index.html',context)

def get_articlesbycategory(request,id):
    categories = category.objects.all()
    cat = category.objects.get(id = id)
    article = Article.objects.filter(category_id=cat)
    context={'cat':cat,'articles':article,'categories':categories}
    return render(request,'articlelist.html',context)

def get_article(request,id):
    categories = category.objects.all()
    article = Article.objects.get(id=id)
    context={'articles':article,'categories':categories}
    return render(request,'articledetail.html',context)

def about(request):
    contexts = Yourself.objects.all()
    names = [context.name for context in contexts]
    email = [context.email for context in contexts]
    phone = [context.phone for context in contexts]
    address = [context.address for context in contexts]
    degree = [context.degree for context in contexts]
    aboutyou=[context.about_you for context in contexts]
    context ={'address': address, 
              'email': email, 
              'phone': phone[0],
              'degree':degree,
              'aboutyou':aboutyou[0]}
    return render(request,'about.html',context)
    
    

def get_Blog(request):
    blog = Blog.objects.all()
    context = {'blogs':blog}
    return render(request,'blogs.html', context)

def get_blogArticle(request, id):
    blogarticle = Blog.objects.get(id=id)
    context ={'blogarticle':blogarticle
    }
    return render(request,'blogArticle.html',context)
    


def get_contact(request):
    contexts = Yourself.objects.all()
    names = [context.name for context in contexts]
    email = [context.email for context in contexts]
    phone = [context.phone for context in contexts]
    address = [context.address for context in contexts]
    linkden = [context.linkedin for context in contexts]
    context ={'address': address, 
              'email': email,
              'phone': phone}
    return render(request,'contact.html',context)

def get_resume(request):
    resume =Resume.objects.all()
    context = {'resume':resume}
    return(request,'resume.html',context)


    



