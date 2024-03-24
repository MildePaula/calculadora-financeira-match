"""
Projeto: Calculadora Financeira

Neste projeto, os alunos criarão uma calculadora financeira em Python que ajudará os
usuários a calcular empréstimos com base em sua renda. A aplicação incluirá as seguintes
etapas:
➔ Validação de Renda:
◆ Os usuários inserirão informações sobre sua renda mensal.
◆ A aplicação verificará se a renda inserida é válida e está dentro de um limite
específico.
➔ Cálculo de Empréstimo:
◆ Após a validação bem-sucedida da renda, os usuários poderão inserir o valor
do empréstimo desejado e o prazo.
◆ A aplicação calculará a taxa de juros apropriada e o valor das prestações
mensais.
➔ Apresentação dos Resultados:
◆ A aplicação exibirá os resultados do cálculo, incluindo o valor das prestações
mensais e o custo total do empréstimo.

IMPLEMENTAÇÃO:
1. Foi adicionado um limite de 30% de empréstimo
2. Foi definido um prazo para pagamento do empréstimo - 24 prestações
"""

class CalculadoraFinanceira:
    def __init__(self):
        pass

    def validar_renda(self, renda):
        return renda >= 2800

    def calcular_limite_emprestimo(self, renda):
        return renda * 0.3

    def validar_emprestimo(self, renda, valor_emprestimo):
        limite_emprestimo = self.calcular_limite_emprestimo(renda)
        return valor_emprestimo <= limite_emprestimo

    def validar_prazo_emprestimo(self, prazo_emprestimo):
        return prazo_emprestimo <= 24

    def calcular_emprestimo(self, valor_emprestimo, prazo_emprestimo):
        taxa_juros = 0.08  
        if prazo_emprestimo > 24:
            prazo_emprestimo = 24
            print("O prazo do empréstimo foi ajustado para o máximo permitido de 24 meses.")
        prestacao_mensal = (valor_emprestimo * taxa_juros) / (1 - (1 + taxa_juros) ** -prazo_emprestimo)
        custo_total = prestacao_mensal * prazo_emprestimo
        return prestacao_mensal, custo_total

    def executar(self):
        renda = float(input("Digite sua renda mensal em R$: "))
        if self.validar_renda(renda):
            limite_emprestimo = self.calcular_limite_emprestimo(renda)
            valor_emprestimo = float(input(f"Digite o valor do empréstimo desejado (até 30% da renda, ou seja, até R${limite_emprestimo:.2f}): "))
            if self.validar_emprestimo(renda, valor_emprestimo):
                prazo_emprestimo = int(input("Digite o prazo do empréstimo em meses (até 24 meses): "))
                if self.validar_prazo_emprestimo(prazo_emprestimo):
                    prestacao_mensal, custo_total = self.calcular_emprestimo(valor_emprestimo, prazo_emprestimo)
                    print(f"\nPrestação mensal: R${prestacao_mensal:.2f}")
                    print(f"Custo total do empréstimo: R${custo_total:.2f}")
                else:
                    print("O prazo do empréstimo não pode exceder 24 meses.")
            else:
                print(f"O valor do empréstimo excede o limite permitido (até 30% da renda, ou seja, até R${limite_emprestimo:.2f}).")
        else:
            print("Sua renda mensal não é válida ou está abaixo do limite de R$2800.")

if __name__ == "__main__":
    calculadora = CalculadoraFinanceira()
    calculadora.executar()
