from django.shortcuts import render
from authors.models import Abstract
from proceedings.models import Session

def home(request, key=None):
    tags_list = []
    session_list = Session.objects.all()
    session = []
    

    
    
    if key != None and key != 'alltag':
        if key == 'poster':
            abstracts = Abstract.objects.filter(delivery_decision='Poster')
        elif key == 'oral':
            abstracts = Abstract.objects.filter(delivery_decision='Oral').order_by('date')
            for item in session_list:
                abstract_ordered = []
                for abstract in abstracts:
                    if item.start <= abstract.date and item.finish >= abstract.date:
                        abstract_ordered.append(abstract)
                
                session.append({'session': item, 'abstracts': abstract_ordered})
        else:
            abstracts = Abstract.objects.filter(tags__contains=key)
    else:
        abstracts = Abstract.objects.order_by('?')

    for abstract in abstracts:
        if abstract.tags != None:
            tags = abstract.tags.split(',')
            tags_list.append(tags)

    tags_1D = sum(tags_list, [])
    for i in range(len(tags_1D)):
        tags_1D[i] = str(tags_1D[i])

    if key == None:
        tags_1D = tags_1D[::8]

    tags_1D = sorted(set(tags_1D))
    
    if key == 'oral':
        return render(request, 'oral.html', {'abstracts': abstracts, 'tags': tags_1D, 'key': key, 'session': session})
    else:
        return render(request, 'proceedings.html', {'abstracts': abstracts, 'tags': tags_1D, 'key': key, 'session': session})


#def abstract(request, key=None):

