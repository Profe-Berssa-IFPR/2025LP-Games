# MostraColor.py
# Este script demonstra como imprimir texto colorido no terminal usando a biblioteca termcolor.
# Certifique-se de que a biblioteca termcolor está instalada, comando para instalar no Terminal: 
# pip install termcolor
from termcolor import colored

# Imprime texto em diferentes cores
print(colored('Este texto é vermelho.', 'red'))
print(colored('Este texto é verde.', 'green'))
print(colored('Este texto é azul.', 'blue'))

# Também é possível adicionar atributos como negrito e cor de fundo
print(colored('Texto amarelo em negrito com fundo cinza.', 'yellow', 'on_grey', ['bold']))