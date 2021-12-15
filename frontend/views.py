import json

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import DocumentForm
from .calculation_sklearn import calculate_scores
from .top_words import calculate_top_words
from django.http import HttpResponse
import csv
import numpy as np

def main_frontend(request):

    if request.method == "POST":

        form = DocumentForm(request.POST)

        if form.is_valid():

            doc1 = str(form.cleaned_data['document_1'])
            doc2 = str(form.cleaned_data['document_2'])
            doc3 = str(form.cleaned_data['document_3'])
            doc4 = str(form.cleaned_data['document_4'])

            tfidf_dataframe = calculate_scores(doc1, doc2, doc3, doc4)
            top_words = calculate_top_words(doc1, doc2, doc3, doc4)

            request.session['dataframe'] = tfidf_dataframe
            # tfidf_dataframe = calculate_scores("Please note that if we did find a problem, we would probably re-run all our regressions with an appropriate linr transformation. ", "What is your p-value for the heteroskedasticity test, and is it significant?", "Is the regression significant? How do you know?", "What is the slope coefficient for black? Is it statistically significant?")
            # top_words = calculate_top_words("Please note that if we did find a problem, we would probably re-run all our regressions with an appropriate linr transformation. ", "What is your p-value for the heteroskedasticity test, and is it significant?", "Is the regression significant? How do you know?", "What is the slope coefficient for black? Is it statistically significant?")

            return render(request, 'frontend.html', {'form': form, 'top_words': top_words,'tfidf_data': tfidf_dataframe })

    else:
        form = DocumentForm(initial={'document_1': 'What is the slope coefficient for male? Is it statistically significant?',
                                     'document_2': 'Please note that if we did find a problem, we would probably re-run all our regressions with an appropriate linr transformation.',
                                     'document_3': 'Is the regression significant? How do you know?',
                                     'document_4': 'What is your p-value for the heteroskedasticity test, and is it significant?',})

    return render(request, 'frontend.html', {'form': form})


def export_to_csv(request):

    if 'dataframe' in request.session:

        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="tfidf_data.csv"'},
        )

        dataframe = request.session['dataframe']
        writer = csv.writer(response)

        for row in dataframe:
            temp = []
            temp.append(row[0])
            for value in row[1]:
                temp.append(value)
            writer.writerow(temp)

        # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
        # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

        return response



    # if request.method == 'POST':
    #     print('Here')
    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = 'attachment; filename="users.csv"'
    #
    #     writer = csv.writer(response)
    #
    #     writer.writerow(['No', 'Token', 'Doc1', 'Doc2', 'Doc3', 'Doc4'])
    #
    #     return response

        # return render(request, 'frontend.html')



    # users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    # for user in users:
    #     writer.writerow(user)


def search(request):
    if request.GET.get('search'):
        search_query = request.GET.get('search')
        # print(search_query)
        if 'dataframe' in request.session:

            dataframe = request.session['dataframe']
            # print(dataframe)
            for value in dataframe:

                if value[0] == search_query:
                    # print(value)
                    # print(np.argsort(value[1][:-1]))

                    return render(request, 'search.html', { 'term' : search_query , 'docs' : np.argsort([i for i in value[1][:-1] if i != 0])})

            return render(request, 'search.html', { 'term' : search_query})

    return render(request, 'search.html')

def search_ajax(request):

    if request.GET.get('search'):
        search_query = request.GET.get('search')
        if 'dataframe' in request.session:
            dataframe = request.session['dataframe']

            for value in dataframe:
                if value[0] == search_query:

                    # print('value', [i for i in value[1][:-1] if i != 0])
                    print(value[1][:-1], np.argsort(value[1][:-1]))
                    temp = {}

                    for index, v in enumerate(value[1][:-1]):
                        if v != 0:
                            temp[v] = index

                    temp = sorted(temp.items(), key=lambda x: x[1])
                    a, b = zip(*temp)

                    data = {'response': b}

                    return JsonResponse(data)



    data = {'response': None}

    return JsonResponse(data)