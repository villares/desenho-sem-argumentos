## `desenho() #0 outubro 2019`

A primeira edição, feita para ser distribuída gratuitamente na [Python Brasil 2019 Ribeirão Preto](https://2019.pythonbrasil.org.br/), é uma espécie de zine, fôlder e pôster. Cada exemplar é para ser único, e foram impressos inicialmente 200.

Veja também [Slides da minha apresentação na Python Brasil](https://abav.lugaralgum.com/palestras/pybr2019/)!

**Muito obrigado a todas as pessoas que apoiaram!**

Agradecimentos especiais: Décio Otoni de Almeida, Bernardo Fontes, Monica Rizzolli

Contribuiram para a impressão: Adri Patamoma, Advan Shumiski, André Burnier, Bernardo Fontes, Fábio C. Barrionuevo da Luz, Juan Lopes, Lucia Dossin, Monica Rizzolli, Otavio Carneiro, Rodolfo Viana, Thais Viana, Uriá Fassina, Yorik van Havre (primeira leva em ordem alfabética).
E também: Dann Luciano e Fábio Souza.

**[Se quiser fazer uma pequena doação.](https://gumroad.com/l/desenho0)**

### Sugestões para executar o cógido do pôster

Para executar o [código da edição #0 outubro 2019](https://github.com/villares/desenho-sem-argumentos/tree/master/0_outubro_2019), instale o Processing modo Python ([instruções](https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/)).

O código de cada elemento do zine está em [estudos](https://github.com/villares/desenho-sem-argumentos/blob/master/0_outubro_2019/estudos/), e tem inclusive versões anteriores abandonadas.

Para gerar apenas a imagem do pôster no verso, execute o código em [poster_r5](https://github.com/villares/desenho-sem-argumentos/tree/master/0_outubro_2019/estudos/poster_r5). O resultado foi depois combinado com a [base_verso.svg](https://github.com/villares/desenho-sem-argumentos/blob/master/0_outubro_2019/estudos/base_poster.svg) na produção do zine.

Usando o [gerador_completo](https://github.com/villares/desenho-sem-argumentos/blob/master/0_outubro_2019/gerador_completo) é possível produzir novas tiragens completas (frente e verso) prontas para imprimir!

### ERRAATA/ATUALIZAÇÃO

No código dos pôsters impressos encontrei alguns erros de indentação confira o código do gerador neste repositório que está OK... minhas desculpas. 

- Na versão inicial impressa havia erros de indentação, no começo da linha do `randomSeed(s)` faltam 4 espaços, e no começo da linha `pass # nao desenha nada!` no final, faltaram 8 espaços. 

- Em dez/2019 encontrei mais um erro de indentação e agora suponho que está tudo certo!
(o código no repositório sempre esteve OK, só a representação dele no SVG que "andou".)

---

```python
desenho() # publicação independente de desenho e programação
""" 
Copyright (C) 2019 Alexandre B A Villares.
Texto e imagens: Licença Atribuição-NãoComercial-CompartilhaIgual 4.0
Código: Licença Pública Geral GNU (GPL v3.0)
"""
```
