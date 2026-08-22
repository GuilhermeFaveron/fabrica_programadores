import streamlit as st

st.sidebar.image('img/logo_carros.jpg') #logo da empresa de vocês
st.sidebar.markdown('# Car Rental') #Nome da empresa de Vocês
numero_carro = 2
lista_carros = ["Porsche gt3 rs", "Golf GTI", "Puro sangue", "GTR R34", "Dodge HellCat"]
detalhes_carro = {
    "Porsche gt3 rs":{"preco":12000, "portas":"2 portas", "cor":"Verde"},
    "Golf GTI":{"preco":2000, "portas": "4 portas", "cor":"Vinho"},
    "Puro sangue":{"preco":20000, "portas":"2 portas", "cor":"Cinza"},
    "GTR R34":{"preco": 55000, "portas":"2 Portas", "cor":"azul"},
    "Dodge HellCat":{"preco": 10000, "portas": "2 portas","cor":"Laranja"}
}
carro_selecionado = st.sidebar.selectbox('Selecione o carro que deseja', lista_carros)
detalhes_selecionado = detalhes_carro[carro_selecionado]

st.title(carro_selecionado)
st.image(f'img/{carro_selecionado}.jpg')

st.subheader("Detalhes do Veículo")


col1, col2, col3 = st.columns(3)


col1.metric("Preço Diária", f'R$ {detalhes_selecionado["preco"]}')
col2.metric("Portas", detalhes_selecionado["portas"])
col3.metric("Cor", detalhes_selecionado["cor"])


st.divider()


qtd_dias = st.number_input("Quantos dias quer ficar com o carro?", 1)



if st.button("Alugar", type="primary"):
    st.success(f'O aluguel do carro vai custar: **R$ {qtd_dias * detalhes_selecionado["preco"]}**')