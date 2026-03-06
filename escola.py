import pytest


def verificador_media(media:int|float) -> str:

      #  testando para ver se a media é um numero
      if not isinstance(media,(int,float)):
            raise TypeError ("Tipo inválido, a entrada deve ser numérica")
      
      if media >= 0 or media <= 10:
            raise ValueError("O valor deve ser maior ou igual a 0 e menor ou igual a 10")
      
      if media >= 0 or media <= 10:
            raise ValueError("O valor deve ser maior ou igual a 0 e menor ou igual a 10")
      
      if media >= 7: 
            return "Aprovado"
      elif media <= 5:
            return "Reprovado"
      else:
            return "Recuperação"
      
      
            
      
            
      
      


if __name__ == "__main__":
      print(verificador_media(media=2))