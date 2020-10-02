# calculadora-de-prazos-datas
Script em Python para ajudar a calcular prazos com base na diferença de dias entre duas datas.

Após data inicial (do tipo string) e um prazo (do tipo inteiro) informados pelo usuário,
haverá a formatação destes dados (conversão do tipo string para o tipo date) e o cálculo será realizado
retornando em tela o prazo final, isto é, data final como resultdado do cálculo entre a data inicial e o prazo 
expresso em quantidade de dias.

O resultado leva em conta o fato de que caso a data final se estabelecer em um sábado ou domingo, os mesmos
não serão contados como dias úteis e por isso a data final será lançada para o próximo dia útil.

Serão apresentados também os calendários quando a última data ultrapassar o mês atual, ou seja, para o mês
subsequente. Caso contrário, somente um calendário será exibido.

Pra finalizar o usuário é questionado se deseja ou não continuar com os cálculos definindo a continuidade 
ou não da execução do script que rodará por meio do executável Calculadora de Prazos (DATA).exe
