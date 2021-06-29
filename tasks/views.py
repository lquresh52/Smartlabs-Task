from django.shortcuts import render,  redirect
from decouple import config
import requests

# Create your views here.
def currency_convertor(request):

    api_key = config('API_KEY')
    url = f'https://free.currconv.com/api/v7/currencies?apiKey={api_key}'


    response = requests.get(url)
    response = response.json()
    country_codes = response['results']

    if request.method != 'POST':
        return render(request, 'currency_convertor.html', context={'country_codes':country_codes, })
    
    amountconvert = float(request.POST.get('amountconvert'))
    fromcurrency = request.POST.get('fromcurrency')
    tocurrency = request.POST.get('tocurrency')


    query = f'{fromcurrency}_{tocurrency}'
    convert_url = f'https://free.currconv.com/api/v7/convert?q={query}&compact=ultra&apiKey={api_key}'

    convert_res = requests.get(convert_url)
    print(convert_res.json())

    converted_amount = amountconvert * convert_res.json()[query]
    return redirect('converted-currency', from_currency=fromcurrency, to_currency=tocurrency, converted_amount=converted_amount, amount=amountconvert, conversion_rate=convert_res.json()[query])


def converted_currency(request, from_currency, to_currency, converted_amount, amount, conversion_rate):
    return render(request, 'converted_currency.html', context={'from_currency':from_currency, 'to_currency':to_currency, 'converted_amount':converted_amount, 'amount':amount, 'conversion_rate':conversion_rate})



