from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def publications(request, collection):
    if collection == '__history__.html':
        return render_to_response(
            'publications/history.html',
            {
            })
    return render_to_response(
                'publications/publications.html',
                {
                    'collection' : collection,
                })

def papers(request, paper):
    if paper == '':
        return HttpResponseRedirect('/publications/')
    return HttpResponseRedirect('/media/' + paper)
