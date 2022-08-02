import streamlit as st;
from streamlit import caching

#Menu/Layout
st.sidebar.title('Fretes e Mudanças')
st.sidebar.markdown('Bem vindo ao serviço de orçamento do Fretes e Mudanças!')
st.sidebar.markdown('Na página ao lado você deverá inserir as informações da viagem e ao final terá todas as informações do seu orçamento.')

#col1, col2, col3 = st.columns(3)

def InfoViagem():
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

    #Custo
    Custo = Distancia * 7
    if (ServicoAdd == 'Sim'):
        Custo = Custo + 100

    #valor do  Orçamento
    st.markdown(' ### O valor do seu orçamento é:')
    st.write("R$", Custo)

    #Botões
    proxViagem = st.button('Próximo', key=('proxViagem'), on_click=InfoContato)
    LimparViagem = st.button('Limpar Formulário', key=('LimparViagem'))
    
def InfoContato():
    st.title('Informações de Contato ')
    Nome = st.text_input('Informe seu nome')
    Contato = st.text_input('Informe um número de telefone para contato')
    Permissao = st.radio('Você autoriza que nossa equipe entre em contato com você?', ('Não', 'Sim'))
    
    #Botões
    proxViagem = st.button('Próximo', key=('proxContato'), on_click=InfoPagamento)
    voltarContato = st.button('Voltar', key=('voltarContato'), on_click=InfoViagem)
    LimparContato = st.button('Limpar Formulário', key=('LimparContato'))
    
def InfoPagamento():
    st.title('Orçamento')
    #st.write('Selecione a forma de pagamento:')
    Pagamento = st.radio('Selecione a forma de pagamento:', ('Cartão de Crédito', 'Débito', 'Pix', 'Boleto'))
    
    #Botões
    proxPagamento = st.button('Próximo', key=('proxPagamento'))
    #if proxPagamento:
     #   st.balloons()
    voltarPagamento = st.button('Voltar', key=('voltarPagamento'), on_click=InfoContato)
    LimparPagamento = st.button('Limpar Formulário', key=('LimparPagamento'))
    
InfoViagem()