# APLICAÇÂO DE MINERAÇÃO DE SENTENÇAS

Desenvolvi uma aplicação em Python para me auxiliar nos estudos de Inglês!

Resumo da opera. Utilizo uma metodologia que aprendi com Mairo Vergara onde realizo a mineração de sentenças diáriamente, consiste em localizar em artigos, séries, noticias, etc... palavras em Inglês que ainda não estão presentes no meu vocabulário, após localizadas eu procuro a definição, a transcrição fonética e um exemplo de uma aplicação das palavras, então adiciono no software Anki que é básicamente uma aplicação de flash card, onde na frente coloco apenas o exemplo da palavra aplicada e no verso coloco a definição e a transcrição fonética.

Bem, o processo acima descrito acaba tomando muito meu tempo de estudo, tempo que eu gostaria de estar praticando lisening. Para solucionar isso desenvolvi um código que trabalha da seguinte forma:

1 - Utilizando um plugin do próprio Anki consigo fazer requisições no meu código Python e coletar qualquer informação das sentenças que já tenho armazenadas;
2 - Utilizando alguns endereços da web coletei as 10.000 palavras mais utilizadas em Ingles e montei um banco de informações;
3 - Com as informações de minhas sentenças e desse banco de palavras realizo uma lógica de comparação, onde a cada execução a aplicação irá coletar 15 palavras que estão presentes nesse banco de palavras, porém, que não estão presentes em meu Anki;
3 -  Utilizando módulo do Bard(IA da Google) para Python, realizo requisições com um prompt, solicitando que a IA me disponibilize:

- A definição de cada uma dessas 15 paravras;
- A transcrição fonética;
- Me disponibilize 3 exemplos de aplicação em frases;

Ao final da aplicação tenho o resultado "new_words_definitions.html" contido na pasta "files", utilizo as informações para alimentar meu Anki.