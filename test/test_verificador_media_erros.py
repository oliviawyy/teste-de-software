import pytest
from escola import verificador_media


def test_string_como_entrada():
    with pytest.raises(TypeError, match="Tipo inválido, a entrada deve ser numérica"):
        verificador_media("OITO")



