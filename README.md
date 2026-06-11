# Otimização Computacional em Inteligência Artificial: Otimização de Word Embeddings

Este repositório contém o projeto prático desenvolvido com o foco no estudo e aplicação de técnicas de Otimização Computacional no processo de treino de modelos de Inteligência Artificial. Mais especificamente, debruça-se sobre a geração de *Word Embeddings* mediante as arquiteturas matemáticas **Skip-Gram com Negative Sampling (SGNS)** e **Noise Contrastive Estimation (NCE)**.

## Sobre o Projeto

O objetivo basilar deste projeto transcende o mero treino de um modelo de Processamento de Linguagem Natural (NLP). O foco central incide sobre o **estudo da dinâmica matemática e computacional inerente a diferentes algoritmos de otimização**, quando submetidos a um problema não-convexo de extrema dimensionalidade.

No decorrer deste estudo, procede-se à comparação rigorosa de três otimizadores fundamentais:
1. **SGD (Stochastic Gradient Descent):** Abordagem estática canónica desprovida de momento.
2. **RMSProp:** Mecanismo com taxa de aprendizagem adaptativa baseada no histórico exponencial de gradientes.
3. **Adam:** Abordagem híbrida avançada (estado-da-arte) que amalgama a métrica de momento com taxas de aprendizagem adaptativas.

## Principais Análises e Visualizações

O projeto encontra-se fundamentado em avaliações analíticas sob a perspetiva da Engenharia e Otimização Computacional:
* **Curvas de Convergência (Loss):** Monitorização do progresso iterativo de otimização de cada algoritmo em ambas as arquiteturas matemáticas.
* **Análise de Eficiência de Pareto:** Avaliação rigorosa de *trade-offs* de Otimização Multiobjetivo, correlacionando o Custo Computacional (Tempo de Execução) com a Qualidade da Convergência (Erro final).
* **Simulação Topológica 3D:** Modelação visual das trajetórias iterativas de cada otimizador numa simulação da *Loss Landscape*. Esta representação evidencia matematicamente o impacto das oscilações direcionais ("zig-zag") do RMSProp e a fluidez de convergência do Adam perante pontos de sela e vales sub-ótimos.
* **Projeção PCA de Clusters Semânticos:** Avaliação qualitativa do *output* da otimização, efetuando a redução de dimensionalidade do hiperespaço vetorial para 2D. Este método permite validar empiricamente se os otimizadores convergiram para representações onde a semântica dita a topologia geométrica (e.g., constelações coerentes de termos associados a realeza, animais e alimentação).

## Tecnologias Utilizadas

* **Python 3**
* **PyTorch:** Arquitetura computacional para o treino de modelos de *Deep Learning* recorrendo a processamento paralelo em GPU (CUDA).
* **Plotly & Matplotlib:** Implementação de visualizações de dados avançadas e representações matemáticas tridimensionais interativas.
* **Pandas & NumPy:** Processamento vetorial e gestão eficiente das métricas registadas durante as fases de treino.

## Como Executar

1. **Clonar o Repositório**
2. **Instalação de Dependências:** 
   O ficheiro `requirements.txt` documenta todas as bibliotecas requeridas. Recomenda-se a sua instalação num ambiente virtual:
   ```bash
   pip install -r requirements.txt
   ```
3. **Pré-Processamento de Dados:**
   Primeiramente, deve ser executado na íntegra o ficheiro `preprocessing.ipynb`. Este *notebook* é responsável pela limpeza do *corpus*, construção do vocabulário, e estruturação das distribuições probabilísticas necessárias para as formulações matemáticas de amostragem negativa.
4. **Treino e Avaliação dos Modelos:**
   Subsequentemente, abre e executa o ficheiro `main.ipynb`. 
   > **Nota Metodológica:** É possível omitir a re-execução das células de treino intensivo iterativo. O código está concebido de modo a facultar o carregamento direto dos modelos otimizados (arquivos `.pth`) a partir da diretoria `saved_models`, permitindo a visualização instantânea da análise de resultados e topologias 3D no ambiente local.

---
*Projeto desenvolvido no âmbito da Unidade Curricular de Otimização Computacional.*
