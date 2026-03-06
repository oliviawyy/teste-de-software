import pytest


def verificador_media(media:int|float) -> str:

      #  testando para ver se a media é um numero
      if not isinstance(media,(int,float)):
            raise TypeError ("Tipo inválido, a entrada deve ser numérica")
      
      if media < 0:
            raise ValueError("Valor inválido, a média não pode ser negativa")
      
      if media > 10:
            raise ValueError("Valor inválido, a média deve ser entre 0 e 10")
      
      if media >= 7: 
            return "Aprovado"
      elif media <= 4:
            return "Reprovado"
      else:
            return "Recuperação"
      
      
            
      
            
      
      


if __name__ == "__main__":
      print(verificador_media(media=2))