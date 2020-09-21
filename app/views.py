from .forms import Leitor
from django.shortcuts import render
from .funcoes import linux, manipulate_txt,write_sequence, data_visualization,remove_barra
from vienn2 import converte_to_string,abre_arquivo,limpar
# Create your views here.


def page_main(request):
    if request.method == 'POST':
        form = Leitor(request.POST)
        if form.is_valid():
            text_area = form.cleaned_data['text_area']
            #retorno = linux(text_area)
            #abre_arquivo()
            limpar(abre_arquivo())
            # str(retorno)
            # print(retorno)


            remove_barra()
            # write_sequence(retorno)
            write_sequence(text_area) # escreve no .fasta a entrada do textarea
            data_visualization()
            #read_sequence()
            linux() # executa o algoritmo com base no .fasta
            #  read_sequence()

            manipulate_txt() # realiza a leitura da saida do algoritmo sankoffAPP
            #converte_to_string(limpar(abre_arquivo()))




            return render(request, 'result.html', {'read':converte_to_string(limpar(abre_arquivo()))})



    else:
        form = Leitor(request.POST)
    return render(request, 'home.html', {'form':form})
