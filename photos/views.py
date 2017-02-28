#import our libraries
from .models import Memes,Comment#import the memes and the comments
from django.shortcuts import render,get_object_or_404,redirect#import some shortcuts
from .forms import PostForm#import the form model

#render the index page
def index(request):
    return render(request,"photos/index.html",{})
def Mistake_redirect(request):
    return redirect('/photos/15')
def detail(request,meme_id):
    #get the memes
     memes=get_object_or_404(Memes,pk=meme_id)

     if request.method=="POST":
         form=PostForm(request.POST)#populate
         if form.is_valid():
             comment=form.cleaned_data['comment']#add the data from the comment 
             name=form.cleaned_data['name']#add the name from the comment 
             meme_title=form.cleaned_data['meme_title']
             Thecomment=Comment.objects.create(name=name,comment=comment,Memetitle=meme_title)#make a new instance of the model
             Thecomment.save()
     else:
            form = PostForm()        
     All_comments=Comment.objects.all()
     
#the contexts, pretty straightforward
     context={
         "name":memes.joker,
         "description":memes.description,
         "photo":memes.photo_link,
         "plus1":memes.id+1,
         "minus1":memes.id-1,
         "meme_id":meme_id,
         "form":form,
         "comment":All_comments,

         }
     
     return render(request,"photos/detail.html",context)
         
#redirect
def PageRedirect(request):
    return redirect('/photos/'+str(Memes.objects.count()+1))
#redirect
def PageMoreRedirect(request):
    return redirect('/photos/1')

#context for the main meme page
def memesPage(request):
    all_memes=Memes.objects.all()
    context={"all_memes":all_memes}
    return render(request,"photos/meme.html",context)  
