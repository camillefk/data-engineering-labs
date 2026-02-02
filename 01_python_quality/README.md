# 1. Refatoração de Pipeline Pandas para Produção (Portuguese Version)
Este projeto documenta o processo de refatoração do script refactoring_pandas.py. O objetivo foi transformar um script antigo em um arquivo Python modular, tipado e documentado, seguindo as melhores práticas da indústria.


## Implementações Técnicas
- Type Hinting (PEP484)
Implementei o uso de tipos estáticos para aumentar previsibilidade de código, assim eu evito erros de execução em pipelines que processam milhões de linhas.

- Docstrings (Google Style)
Aprendi que "#" são comentários no código para mim mesma, que me ajude a entender a lógica do que estou fazendo. Enquanto """ ... """ explica como usar uma função para outras pessoas.
Aprendi também sobre a Anatomia do Padrão Google:
    1. Resumo: O que a função faz (o verbo tem que está no imperativo);
    2. Argumentos: Tenho que listar cada parâmetro, seu tipo e o que significa;
    3. Retorno: O que sai da função;
    4. Raises: Dizer o que pode dar errado, crucial no uso de try/except.

- Modularização e Funções Puras
Uma função pura é aquela que nao tem efeitos colaterais e retorna sempre o mesmo resultado quando a entrada sempre for a mesma. É importante pq são fáceis de testar

## Automoção e Qualidade de Código
Para garantir que a qualidade se mantenha constante, integrei ferramentas de análise estática e formatação:
    1. Black - Formatação automática 
    2. Pylint - Análise estática

----------------------------------------------------------------------------------

# 1. Refactoring a Pandas Pipeline for Production (English Version)
This project documents the process of refactoring the refactoring_pandas.py script. The goal was to transform a legacy script into a modular, typed, and well-documented Python Filo, following industry best practices.


## Technical Implementations
- Type Hinting (PEP484) 
I implemented static type hints to improve code predictability and prevent runtime errors in pipelines that process millions os rows.

- Docstring (Google Style)
I learned that # comments are primarily for myself, helping me understand the logic I'm implementing, while """...""" docstrings explain how to use a function for others.
I also learned about the Google Docstring Anatomy:
    1. Summary: What the function does (the verb should be in the imperative mood);
    2. Arguments: A list of each parameter, its type, and its purpose;
    3. Returns: What the function outputs;
    4. Raises: What can go wrong — crucial when using try/except.

- Modularization and Pure Functions
A pure function is one that has no side effects and always returns the same output given the same input.
This is important because pure functions are easy to test and reason about.

## Automation and Code Quality
To ensure consistent code quality, I integrated static analysis and formatting tools:
    1. Black - automatic code formatting
    2. Pylint - static code analysis

----------------------------------------------------------------------------------