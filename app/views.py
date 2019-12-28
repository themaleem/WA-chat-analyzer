from django.shortcuts import render
import re
from .models import Files
# Create your views here.

def index(request):
    if request.method=='POST':
        if 'file' in request.FILES:
            file=request.FILES.get('file')
            new_file=Files.objects.create(upload=file)
            new_file.save()
            print(file,type(new_file.upload))

            with open(new_file.upload.path,'rb') as file:
            #initialize a variable (file_content) for byte-like string with b''
            #and add each line in the file to vaiable 
                file_content=''    
                for i in file:
                    #amount_of word=sum()
                    file_content+=i.decode('utf-8')
                print(get_chatters(file_content))

        else:
            print('no file uploaded')
    context={
        
    }
    return render(request,'app/index.html',context)


# refer to https://github.com/themaleem/PythonScripts/blob/master/scripts/wa_chatters.py 
def get_chatters(file_content):
    chatters=[]
    text=re.compile(r'\d\d/\d\d/\d\d\d\d, \d\d:\d\d - (.*:)') 
    patterns=re.findall(text,file_content)
    for i in patterns:
        i=i.split(':')[0]        
        #   append sender's name if not already in chatter's list
        if i not in chatters: 
            chatters.append(i)
    return chatters