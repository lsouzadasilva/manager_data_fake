import streamlit as st
from faker import Faker
import pandas as pd
import random

# Inicializa o Faker
fake = Faker('pt_BR')

# Configurações da página
st.set_page_config(
    page_title="Manager Data Fake",
    page_icon="📊",
    layout="centered",
)

def ocult_menu():
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)
ocult_menu()

# Função para gerar dados falsos baseados na categoria selecionada
def gerar_dados_falsos(categoria, num_linhas, num_colunas):
    dados = []
    
    for _ in range(num_linhas):
        linha = {}
        
        # ID sempre será um CPF falso
        linha['CPF'] = fake.cpf()
        
        # Gera dados específicos para cada categoria
        if categoria == 'Automotivo':
            linha['Marca do Veículo'] = fake.company()
            linha['Modelo do Veículo'] = fake.word()
            linha['Ano de Fabricação'] = random.randint(1990, 2025)
            linha['Quilometragem'] = random.randint(0, 200000)
            linha['Tipo de Combustível'] = fake.random_element(elements=('Gasolina', 'Diesel', 'Elétrico','Hibrido'))
            linha['Cor do Veículo'] = fake.color_name()
            linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Multas?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Valor do Veículo'] = random.randint(20000, 200000)
            linha['Tipo de Câmbio'] = fake.random_element(elements=('Manual', 'Automático'))
            linha['Número de Portas'] = random.randint(2, 4)
            linha['Tem Airbag?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem ABS?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data da Última Revisão'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
        
        elif categoria == 'Imobiliário':
            linha['Endereço do Imóvel'] = fake.address()
            linha['Tipo de Imóvel'] = fake.random_element(elements=('Casa', 'Apartamento', 'Terreno'))
            linha['Área do Imóvel (m²)'] = random.randint(50, 1000)
            linha['Valor do Imóvel'] = random.randint(60000, 1000000)
            linha['Número de Quartos'] = random.randint(1, 5)
            linha['Número de Banheiros'] = random.randint(1, 3)
            linha['Tem Garagem?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Piscina?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Elevador?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Condomínio Fechado?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Valor do Condomínio'] = random.randint(150, 2000)
            linha['Ano de Construção'] = random.randint(1980, 2024)
            linha['Tipo de Oferta'] = fake.random_element(elements=('Venda', 'Aluguel'))
            linha['Data da Última Reforma'] = fake.date_between(start_date='-10y', end_date='today').strftime('%d/%m/%Y')
        
        elif categoria == 'Serviços financeiros (cartão de crédito)':
            linha['Número do Cartão'] = fake.credit_card_number()
            linha['Validade do Cartão'] = fake.credit_card_expire()
            linha['Limite do Cartão'] = random.randint(300, 20000)
            linha['Tem Anuidade?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Cashback?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Bandeira do Cartão'] = fake.credit_card_provider()
            linha['Dia de Vencimento da Fatura'] = random.randint(1, 31)
            linha['Valor da Última Fatura'] = random.randint(0, 20000)
            linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Programa de Pontos?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Número de Parcelas em Aberto'] = random.randint(0, 12)
            linha['Valor Total de Parcelas'] = random.randint(1000, 10000)
            linha['Tem Limite Internacional?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data de Emissão do Cartão'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
        
        elif categoria == 'Serviços financeiros (seguros)':
            linha['Tipo de Seguro'] = fake.random_element(elements=('Automóvel', 'Vida', 'Residencial'))
            linha['Seguradora'] = fake.company()
            linha['Valor do Prêmio Mensal'] = random.randint(100, 1000)
            linha['Valor da Cobertura'] = random.randint(50000, 500000)
            linha['Tem Franquia?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Valor da Franquia'] = random.randint(500, 5000)
            linha['Data de Início do Seguro'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Término do Seguro'] = fake.date_between(start_date='today', end_date='+5y').strftime('%d/%m/%Y')
            linha['Número de Sinistros'] = random.randint(0, 5)
            linha['Tem Cobertura Internacional?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Assistência 24h?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tipo de Pagamento'] = fake.random_element(elements=('Mensal', 'Anual'))
            linha['Tem Desconto por Fidelidade?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data do Último Sinistro'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
        
        elif categoria == 'Serviços financeiros (empréstimos)':
            linha['Valor do Empréstimo'] = random.randint(1000, 100000)
            linha['Taxa de Juros (%)'] = round(random.uniform(1.0, 10.0), 2)
            linha['Número de Parcelas'] = random.randint(12, 60)
            linha['Valor da Parcela'] = random.randint(50, 5000)
            linha['Tipo de Empréstimo'] = fake.random_element(elements=('Pessoal', 'Consignado'))
            linha['Instituição Financeira'] = fake.company()
            linha['Data de Contratação'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Vencimento'] = fake.date_between(start_date='today', end_date='+5y').strftime('%d/%m/%Y')
            linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Taxa de Adiantamento?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Número de Parcelas Pagas'] = random.randint(0, 60)
            linha['Número de Parcelas em Atraso'] = random.randint(0, 12)
            linha['Tem Restrição no Nome?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Motivo do Empréstimo'] = fake.random_element(elements=('Reforma', 'Viagem', 'Educação'))
        
        elif categoria == 'Serviços financeiros (consórcios)':
            linha['Tipo de Consórcio'] = fake.random_element(elements=('Automóvel', 'Imóvel'))
            linha['Valor do Bem'] = random.randint(50000, 500000)
            linha['Número de Cotas'] = random.randint(12, 120)
            linha['Valor da Cota'] = random.randint(500, 5000)
            linha['Taxa Administrativa (%)'] = round(random.uniform(0.5, 5.0), 2)
            linha['Data de Início'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Término'] = fake.date_between(start_date='today', end_date='+10y').strftime('%d/%m/%Y')
            linha['Número de Cotas Pagas'] = random.randint(0, 120)
            linha['Número de Cotas em Atraso'] = random.randint(0, 12)
            linha['Tem Lance Fixo?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Valor do Lance'] = random.randint(1000, 10000)
            linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Reajuste Anual?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data da Última Assembléia'] = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
        
        elif categoria == 'Serviços financeiros (financiamento)':
            linha['Tipo de Financiamento'] = fake.random_element(elements=('Imóvel', 'Veículo'))
            linha['Valor Financiado'] = random.randint(50000, 500000)
            linha['Taxa de Juros (%)'] = round(random.uniform(1.0, 10.0), 2)
            linha['Número de Parcelas'] = random.randint(12, 360)
            linha['Valor da Parcela'] = random.randint(500, 5000)
            linha['Data de Início'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Término'] = fake.date_between(start_date='today', end_date='+30y').strftime('%d/%m/%Y')
            linha['Número de Parcelas Pagas'] = random.randint(0, 360)
            linha['Número de Parcelas em Atraso'] = random.randint(0, 12)
            linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Reajuste Anual?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Valor da Entrada'] = random.randint(10000, 100000)
            linha['Tem Restrição no Nome?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Motivo do Financiamento'] = fake.random_element(elements=('Casa Própria', 'Carro Novo'))
        
        elif categoria == 'Marketing':
            linha['Canal de Marketing'] = fake.random_element(elements=('Instagram', 'Google Ads', 'Facebook'))
            linha['Custo por Clique (CPC)'] = round(random.uniform(0.5, 5.0), 2)
            linha['Taxa de Conversão (%)'] = round(random.uniform(1.0, 10.0), 2)
            linha['Número de Cliques'] = random.randint(100, 10000)
            linha['Número de Conversões'] = random.randint(10, 1000)
            linha['Custo por Aquisição (CPA)'] = round(random.uniform(10.0, 100.0), 2)
            linha['Tem Campanha Ativa?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Orçamento Total'] = random.randint(1000, 100000)
            linha['Gasto Atual'] = random.randint(500, 50000)
            linha['Tipo de Anúncio'] = fake.random_element(elements=('Vídeo', 'Banner', 'Texto'))
            linha['Público-Alvo'] = fake.random_element(elements=('18-35 anos', '35-50 anos', '50+ anos'))
            linha['Tem Retargeting?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data de Início da Campanha'] = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Término da Campanha'] = fake.date_between(start_date='today', end_date='+1y').strftime('%d/%m/%Y')
        
        elif categoria == 'Contábil':
            linha['Renda Mensal'] = random.randint(1318, 20000)
            linha['Tipo de Contribuinte'] = fake.random_element(elements=('PF', 'PJ'))
            linha['Valor do Imposto Pago'] = random.randint(500, 5000)
            linha['Tem Débitos Pendentes?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Número de Dependentes'] = random.randint(0, 5)
            linha['Tem Imóvel em Nome?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Veículo em Nome?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Investimentos?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Valor dos Investimentos'] = random.randint(10000, 100000)
            linha['Tem Declaração Anual?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data da Última Declaração'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Tem Restrição na Receita?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Benefícios Fiscais?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tipo de Regime Tributário'] = fake.random_element(elements=('Simples Nacional', 'Lucro Real'))
        
        # Limita o número de colunas
        if len(linha) > num_colunas:
            linha = dict(list(linha.items())[:num_colunas])
        
        dados.append(linha)
    
    return pd.DataFrame(dados)

# Interface do Streamlit
st.title('📊 Data Fake')
st.markdown("""
    **Desenvolvido por Leandro Souza**  
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leandro-souza-bi/)
    [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lsouzadasilva)
""")

st.markdown("---")

image_path = 'image/fake.png'

# Banner
st.image(image_path, use_container_width=True)

# Descrição
st.markdown("""
    Bem-vindo ao **Gerador de Dados Falsos**!  
    Aqui você pode criar dados fictícios para diversos segmentos, como automotivo, imobiliário, serviços financeiros e muito mais.  
    Selecione a categoria, o número de linhas e colunas, e clique em **Gerar Dados**.
""")

# Seleção da categoria
categoria = st.selectbox(
    '**Selecione a categoria**',
    ['Automotivo', 'Imobiliário', 'Serviços financeiros (cartão de crédito)', 
     'Serviços financeiros (seguros)', 'Serviços financeiros (empréstimos)', 
     'Serviços financeiros (consórcios)', 'Serviços financeiros (financiamento)', 
     'Marketing', 'Contábil']
)

# Seleção do número de linhas e colunas
col1, col2 = st.columns(2)
with col1:
    num_linhas = st.slider('**Número de linhas**', 1, 100000, 10)
with col2:
    num_colunas = st.slider('**Número de colunas**', 1, 15, 5)

# Botão para gerar os dados
if st.button('**Gerar Dados**', type="primary"):
    st.markdown("---")
    st.subheader("Dados Gerados")
    dados = gerar_dados_falsos(categoria, num_linhas, num_colunas)
    st.dataframe(dados.style.highlight_max(axis=0),hide_index=True, use_container_width=True)
    
    # Opção para baixar os dados como CSV
    st.download_button(
        label="📥 Baixar dados como CSV",
        data=dados.to_csv(index=False).encode('utf-8'),
        file_name=f'dados_falsos_{categoria}.csv',
        mime='text/csv',
    )
