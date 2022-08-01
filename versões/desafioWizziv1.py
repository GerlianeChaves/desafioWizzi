#!/usr/bin/env python3

#Desafio Wizzi: Gerliane Chaves

#imports
import streamlit as st
import pandas as pd
#import plotly.express as px
#import plotly.graph_objects as go

#st.write(""" # My first app""")
#st.write("""Hello *world!*""")
     
def InfoViagem():
    st.title('Informações da viagem ')
    LocalPartida = st.text_input('Local de Partida (Cidade/Estado)', key='1s')
    LocalDestino = st.text_input('Local de Destino (Cidade/Estado)', key='2e')
    Distancia = st.number_input('Informe a distância em quilômetros (km)')
    
    Custo = Distancia * 7
    
    #st.write('Para simples conferência:', LocalPartida, LocalDestino, Distancia, Custo)
    
    #Data = st.text_input('Informe a data viagem')
    Data = st.date_input('Selecione a data da viagem')
    InfoAdd = st.text_input('Informações adicionais (condições da estrada, etc)', key='3w')
    
    #serviço adicional
    ServicoAdd = st.radio('Deseja Contratar Serviço adicional?', ('Não', 'Sim'))
    if (ServicoAdd == 'Sim'):
        st.markdown('### Serviços adicionais oferecidos:')
        carregador = st.checkbox('Carregador de móveis')
        carregador = st.checkbox('Ciaxas para embalagem')
        carregador = st.checkbox('Seguro viagem')

    #st.write('Para simples conferência:', LocalPartida, LocalDestino, Distancia)
    #if (st.Button('Submit'))

def InfoContato():
    st.title('Informações de Contato ')
    Nome = st.text_input('Informe seu nome', key='42')
    Contato = st.text_input('Informe um número de telefone para contato', key='5j')
    Permissao = st.radio('Você autoriza que nossa equipe entre em contato com você?', ('Não', 'Sim'))
    
def Orcamento():
    st.title('Orçamento')
    st.write('Serviços Contratados:')
    
    #tabela
    #st.write('Transporte de mudanças entre ', LocalPartida, LocalDestino)
    
    st.write('Clique em próximo para finalizar a compra ou em limpar tudo para cancelar.')
       
    st.info("Entre em contato com nossos colaboradores caso deseje negociar o valor.")

    
def Prox():
    st.button('Próximo')
    
def Voltar():
    st.button('Voltar', key='2')
    
def LimparTudo():
    st.button('Limpar Tudo', key='3')

            
InfoViagem()
Prox() 
Voltar()
LimparTudo()

#InfoContato()
#Orcamento()

if (st.button('Próximo')):
    InfoContato()
#    if (InfoContato()):
 #      Orcamento()
  #  if (Orcamento()):
   #    st.success("Seu orçamento foi enviado com sucesso! Um de nossos colaboradores entrará em contato com você em breve.")

   
  #  if (InfoViagem()):
   #     InfoContato()
   # if InfoContato():
    #    Orcamento()
    #if Orcamento():
     #   st.success("Seu orçamento foi enviado com sucesso! Um de nossos colaboradores entrará em contato com você em breve.")

    


#---------------------------
# success
#st.success("Success")
 
# success
#st.info("Information")
 
# success
#st.warning("Warning")
 
# success
#st.error("Error")
    
    

