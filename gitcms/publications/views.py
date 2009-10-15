from django.shortcuts import render_to_response

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
