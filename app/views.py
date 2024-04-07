from django.shortcuts import render,redirect
from .forms import PytjaForm  # Ensure the correct form is being imported
from .models import *
from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import PytjaForm  # Import your PytjaForm here

def kontakti_view(request):
    if request.method == 'POST':
        form = PytjaForm(request.POST)

        emri = request.POST.get('emri',' ')
        email = request.POST.get('email',' ')
        teksti = request.POST.get('teksti',' ')
        pytja = Pytje(EmriMbiemri=emri,Email = email , Pytja=teksti)
        pytja.save()  # If this form is a ModelForm
        messages.success(request, "Pytja u dergua me Sukses !")
        # if form.is_valid():
            # form.save()  # If this form is a ModelForm
            # Process valid form data here if needed
            # return redirect('index')  # Redirect to the 'index' page

    return render(request, 'contact.html')



# def index(request):
#     data = Njoftime.objects.all()[::-1]
#     latest_video = Video.objects.latest('id')  # Assuming 'id' is the primary key
#     video_id = latest_video.Video_Youtube.split('=')[-1]  # Extract video ID from YouTube URL
#     video_embed_url = f"https://www.youtube.com/embed/{video_id}"  # Construct embed URL
#     title = latest_video.Emri
#     date = latest_video.Data
#     context = {
#         'data': data,
#         "latest_video": latest_video,
#         "video_embed_url": video_embed_url,  # Pass the embed URL to the template
#         "title":title,
#         "date":date,
#     }
#     return render(request, 'index.html', context)

def index(request):
    data = Njoftime.objects.all()[::-1]
    videos_first = Video.objects.all()[::-1]      #.order_by('-id')  # Fetch all videos
    video_lasts = Video.objects.all()[::-1]       #.order_by('-id')  # Fetch all videos

    context = {
        'data': data,
        "videos": videos_first[:4],  # Pass all videos to the template
        "video_lasts": video_lasts[2:],  # Pass all videos to the template
    }
    return render(request, 'index.html', context)



def testo(request):
    import os 
    file_path = os.path.abspath(__file__)

    file_name = os.path.basename(file_path)
    # with open('C:\\Users\\User\\Desktop\\New folder (3)\\project\\app\\views.py','w') as e:
        # e.write('A')
        # e.close()
        # pass
