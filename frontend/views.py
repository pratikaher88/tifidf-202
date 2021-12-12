from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import DocumentForm
from .calculation_sklearn import calculate_scores
from django.http import HttpResponse
import csv

def main_frontend(request):

    if request.method == "POST":

        form = DocumentForm(request.POST)

        if form.is_valid():

            doc1 = str(form.cleaned_data['document_1'])
            doc2 = str(form.cleaned_data['document_2'])
            doc3 = str(form.cleaned_data['document_3'])
            doc4 = str(form.cleaned_data['document_4'])

            # tfidf_dataframe = calculate_scores(doc1, doc2, doc3, doc4)

            tfidf_dataframe = calculate_scores("Please note that if we did find a problem, we would probably re-run all our regressions with an appropriate linr transformation. ", "What is your p-value for the heteroskedasticity test, and is it significant?", "Is the regression significant? How do you know?", "What is the slope coefficient for black? Is it statistically significant?")

            # [(i, j) for i, j in zip(tfidf_dataframe.columns.tolist(), tfidf_dataframe.values.to_list())]

            return render(request, 'frontend.html', {'form': form, 'tfidf_data': tfidf_dataframe })

    else:
        form = DocumentForm()

    return render(request, 'frontend.html', {'form': form})


def export_users_csv(request):

    print('Here', request)

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
