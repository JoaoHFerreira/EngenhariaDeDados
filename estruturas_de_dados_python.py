# Listas em python tem tipagem dinâmica
eu_sou_uma_lista =  ["string", 1.9, 2, True]


# Dicionário, chave valor -> hashmap em java, ele otimiza o método para encontrar índices
# Não pode ter chaves repetidas
eu_sou_um_dicionário = {
    "chave_1" : "valor1",
    2: "outro_valor"
}

# A chave é única e os valores podem se repetir
eu_sou_um_dicionario = {
    "Miraceli": 2000000,
    "Gabriel": 1500000,
    "joao": 1250000,
    "pedro": 1250000,
}

# Tuplas , uma combinação de dados. Valores que só fazem sentido juntos
eu_sou_uma_tupla_de_coordenadas_latitude_longitude = (1111, 234) 

# Set ele uma estrututura desordenada e sem duplicidade, como se fosse um dicionário só com chaves
eu_sou_um_set = {1,2,3,4, "number", "number"}


# Quer saber mais, acesse https://docs.python.org/3/tutorial/datastructures.html


# Os valores dessas estruturas de dados podem se mesclar
dicionario_com_listas_e_tuplas_e_sets = {
    "chave 1": {1,2,3,4,5},
    "chave 2": [1,3,4,5,6,8],
    "chave 3": (1,2)
}

lista_com_dicionarios_tuplas_e_sets = [
    {"chave": "valor"},
    (1,2),
    {"um", "dois"}
    ]
