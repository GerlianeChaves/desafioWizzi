import streamlit as st;
from streamlit import caching
# from gsheetsdb import connect
#from shillelagh.backends.apsw.db import connect

#Menu/Layout
st.sidebar.title('Fretes e Mudanças')
st.sidebar.markdown('Bem vindo ao serviço de orçamento do Fretes e Mudanças!')
st.sidebar.markdown('Na página ao lado você deverá inserir as informações da viagem para que seu orçamento possa ser realizado.')

def InfoViagem():
    with st.form('InfoViagem'):
        st.title('Informações da viagem ')
        LocalPartida = st.text_input('Local de Partida (Cidade/Estado)')
        LocalDestino = st.text_input('Local de Destino (Cidade/Estado)')
        Distancia = st.number_input('Informe a distância em quilômetros (km)')      
        Data = st.date_input('Selecione a data da viagem')
        InfoAdd = st.text_input('Informações adicionais (condições da estrada, etc)')
        
        #serviço adicional
        ServicoAdd = st.radio('Deseja Contratar Serviço adicional?', ('Não', 'Sim'))
        if (ServicoAdd == 'Sim'):
            st.markdown('### Serviços adicionais oferecidos:')
            carregador = st.checkbox('Carregador de móveis')
            embalagem = st.checkbox('Ciaxas para embalagem')
            Seguro = st.checkbox('Seguro viagem')

        #Botões
        proxViagem = st.form_submit_button('Próximo', on_click=InfoContato)
        LimparViagem = st.form_submit_button('Limpar Formulário')
        
def InfoContato():
    with st.form('InfoContato'):
        st.title('Informações de Contato ')
        Nome = st.text_input('Informe seu nome')
        Contato = st.text_input('Informe um número de telefone para contato')
        Permissao = st.radio('Você autoriza que nossa equipe entre em contato com você?', ('Não', 'Sim'))
        
        #Botões
        proxViagem = st.form_submit_button('Próximo', on_click=InfoPagamento)
        voltarContato = st.form_submit_button('Voltar', on_click=InfoViagem)
        LimparContato = st.form_submit_button('Limpar Formulário')
    
def InfoPagamento():
    with st.form('InfoPagamento'):
        st.title('Orçamento')
        Pagamento = st.radio('Selecione a forma de pagamento:', ('Cartão de Crédito', 'Débito', 'Pix', 'Boleto'))
        
        #Botões
        proxPagamento = st.form_submit_button('Próximo')
        #if proxPagamento:
        #   st.balloons()
        voltarPagamento = st.form_submit_button('Voltar', on_click=InfoContato)
        LimparPagamento = st.form_submit_button('Limpar Formulário')

InfoViagem()