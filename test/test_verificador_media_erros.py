import pytest
from escola import verificador_media


def test_string_como_entrada():
    with pytest.raises(TypeError, match="Tipo inválido, a entrada deve ser numérica"):
        verificador_media("OITO")

def test_numero_negativo():
    with pytest.raises(ValueError, match="Valor inválido, a média não pode ser negativa"):
        verificador_media(-5)

def test_media_acima_de_10():
    with pytest.raises(ValueError, match="Valor inválido, a média deve ser entre 0 e 10"):
        verificador_media(2000)


