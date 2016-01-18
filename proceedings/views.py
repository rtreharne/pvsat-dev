from django.shortcuts import render
from authors.models import Abstract

def home(request, key=None):
    tags_list = []
    
    if key != None:
        abstracts = Abstract.objects.filter(tags__contains=key)
    else:
        abstracts = Abstract.objects.all()

    for abstract in abstracts:
        if abstract.tags != None:
            tags = abstract.tags.split(',')
            tags_list.append(tags)

    tags_1D = sum(tags_list, [])
    for i in range(len(tags_1D)):
        tags_1D[i] = str(tags_1D[i])

    tags_1D = sorted(set(tags_1D))
    
    return render(request, 'proceedings.html', {'abstracts': abstracts, 'tags': tags_1D})

