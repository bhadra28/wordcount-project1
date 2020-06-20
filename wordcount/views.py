from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['Fulltext']
    dict={}
    listofwords=fulltext.split()
    for word in listofwords:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    sortedlist=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'dict':dict,'count':len(listofwords),'sorted':sortedlist})

def about(request):
    return render(request,'about.html')
