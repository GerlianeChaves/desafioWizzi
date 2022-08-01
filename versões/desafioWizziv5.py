import streamlit as st;

#Menu/Layout
st.sidebar.title('Fretes e Mudanças')
st.sidebar.markdown('Bem vindo ao serviço de orçamento do Fretes e Mudanças!')
st.sidebar.markdown('Na página ao lado você deverá inserir as informações da viagem e ao final terá todas as informações do seu orçamento.')
#st.sidebar.button('Orçamento Final:')
#botaoSelecionada = st.button('Proximo')
#botaoSelecionada = st.button('Voltar')
#botaoSelecionada = st.sidebar.selectbox('Menu', ['Informação da Viagem', 'Informação de Contato', 'Orçamento Final'])

def InfoViagem():
    st.title('Informações da viagem ')
    LocalPartida = st.text_input('Local de Partida (Cidade/Estado)', key='1s')
    LocalDestino = st.text_input('Local de Destino (Cidade/Estado)', key='2e')
    Distancia = st.number_input('Informe a distância em quilômetros (km)')
        
    Custo = Distancia * 7
        
    Data = st.date_input('Selecione a data da viagem')
    InfoAdd = st.text_input('Informações adicionais (condições da estrada, etc)', key='3w')
        
    #serviço adicional
    ServicoAdd = st.radio('Deseja Contratar Serviço adicional?', ('Não', 'Sim'))
    if (ServicoAdd == 'Sim'):
        st.markdown('### Serviços adicionais oferecidos:')
        carregador = st.checkbox('Carregador de móveis')
        carregador = st.checkbox('Ciaxas para embalagem')
        carregador = st.checkbox('Seguro viagem')

    st.write("O valor estimado é: R$", Custo)
    
def InfoContato():
    st.title('Informações de Contato ')
    Nome = st.text_input('Informe seu nome', key='42')
    Contato = st.text_input('Informe um número de telefone para contato', key='5j')
    Permissao = st.radio('Você autoriza que nossa equipe entre em contato com você?', ('Não', 'Sim'))
    
def InfoPagamento():
    st.title('Orçamento')
    st.write('Selecione a forma de pagamento:')
    Permissao = st.radio('Como deseja pagar:', ('Cartão de Crédito', 'Débito', 'Pix', 'Boleto'))


#Construindo layout
col1, col2 = st.columns(2)
Paginas_info = ['Informações da Viagem', 'Informações de Contato', 'Informações de Pagamento']

telas = col1.radio('#Informações para Orçamento', Paginas_info, key=('telas'))
prox = st.button('Próximo', key=('prox'))

if prox:
    if st.session_state['telas'] == 'Informações da Viagem':
        st.session_state.telas = InfoContato()
    elif st.session_state['telas'] == 'Informações da Contato':
        st.session_state.telas = InfoPagamento()

#Menu
if telas == 'Informações da Viagem':
    col2.write(InfoViagem())
elif telas == 'Informações de Contato':
    col2.write(InfoContato())
elif telas == 'Informações de Pagamento':
    col2.write(InfoPagamento())
        