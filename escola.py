import pytest


def verificador_media(media:int|float) -> str:
      try:
            if media >= 7: 
                  return "Aprovado"
            elif media < 4:
                  return "Reprovado"
            else:
                  return "Recuperação"
            
      except(ValueError):
            return ValueError("O numero deve ser entre 0 e 10")
      except(TypeError):
            return ValueError("A média deve ser um número")
      


if __name__ == "__main__":
      print(verificador_media(media=2))