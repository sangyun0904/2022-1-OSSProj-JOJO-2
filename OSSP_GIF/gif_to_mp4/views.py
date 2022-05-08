from django.shortcuts import render
from .forms import URLform
from django.views import View
# Create your views here.
class MainView(View): 
    template_name = 'gif_to_mp4/main.html'

    def get(self, request):
        form = URLform()
        ctx = {'form':form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = URLform(request.POST)
        print(form['youtube_link'].value())
        #print(form['your_name'])
        #ctx = {'form':form}
        ctx = {'form':form}
        return render(request, self.template_name,ctx)