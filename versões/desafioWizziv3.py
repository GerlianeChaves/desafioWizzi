import streamlit as st;

#Menu/Layout
st.sidebar.title('Fretes e Mudanças')
st.sidebar.markdown('Bem vindo ao serviço de orçamento do Fretes e Mudanças!')
st.sidebar.markdown('Na página ao lado você deverá inserir as informações da viagem e ao final terá todas as informações do seu orçamento.')
#st.sidebar.button('Orçamento Final:')
#botaoSelecionada = st.button('Proximo')
#botaoSelecionada = st.button('Voltar')
botaoSelecionada = st.sidebar.selectbox('Menu', ['Informação da Viagem', 'Informação de Contato', 'Orçamento Final'])

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

if botaoSelecionada == 'Informação da Viagem':
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

if botaoSelecionada == 'Informação de Contato':

# ------------- Inicio Contato --------------
    with st.form(key='InfoViagem'):
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
        input_button_submit_viagem = st.form_submit_button('Próximo')
# ------------- Fim Viagem --------------

    with st.form(key='InfoContato'): 
        st.title('Informações de Contato ')
        Nome = st.text_input('Informe seu nome', key='42')
        Contato = st.text_input('Informe um número de telefone para contato', key='5j')
        Permissao = st.radio('Você autoriza que nossa equipe entre em contato com você?', ('Não', 'Sim'))
        input_button_submit = st.form_submit_button('Próximo')
    
    with st.form(key='Orcamento'): 
        st.title('Orçamento')
        st.write('Serviços Contratados:')

    if input_button_submit_viagem:
        InfoContato()
        st.success('sucess')

if botaoSelecionada == 'Orçamento Final':
    st.title('Orçamento')
    st.write('Serviços Contratados:')
    
    #tabela
    #st.write('Transporte de mudanças entre ', LocalPartida, LocalDestino)
    
    st.write('Clique em próximo para finalizar a compra ou em limpar tudo para cancelar.')
       
    st.info("Entre em contato com nossos colaboradores caso deseje negociar o valor.")    
