
import json
import uuid
from pathlib import Path
from datetime import datetime

# ============================================================
# CONFIGURAÇÃO DO BANCO DE DADOS JSON
# ============================================================

PASTA = Path(__file__).resolve().parent
ARQUIVO = PASTA / "cards_salvos.json"


# ============================================================
# LER CONJUNTOS SALVOS
# ============================================================

def listar_conjuntos():

    if not ARQUIVO.exists():
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return dados if isinstance(dados, list) else []

    except (json.JSONDecodeError, OSError):
        return []


# ============================================================
# SALVAR NOVO CONJUNTO
# ============================================================

def salvar_conjunto(materia, tema, cards):

    conjuntos = listar_conjuntos()

    novo_conjunto = {
        "id": str(uuid.uuid4()),
        "materia": materia,
        "tema": tema,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "cards": [
            {
                "pergunta": pergunta,
                "resposta": resposta
            }
            for pergunta, resposta in cards
        ]
    }

    conjuntos.append(novo_conjunto)

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            conjuntos,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

    return novo_conjunto["id"]


# ============================================================
# CARREGAR UM CONJUNTO
# ============================================================

def carregar_conjunto(id_conjunto):

    conjuntos = listar_conjuntos()

    for conjunto in conjuntos:

        if conjunto["id"] == id_conjunto:
            return conjunto

    return None


# ============================================================
# EXCLUIR UM CONJUNTO
# ============================================================

def excluir_conjunto(id_conjunto):

    conjuntos = listar_conjuntos()

    conjuntos = [
        conjunto
        for conjunto in conjuntos
        if conjunto["id"] != id_conjunto
    ]

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            conjuntos,
            arquivo,
            ensure_ascii=False,
            indent=4
        )
