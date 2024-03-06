# Descrição função para converter velocidade de KM/H para M/S e de M/S para KM/H.
def converterVelocidade(velocidade, unitVelocidade, unitConvert):
    if unitVelocidade == 'K' and unitConvert == 'M':
        return velocidade / 3.6;
    elif unitVelocidade == 'M' and unitConvert == 'K':
        return velocidade * 3.6;
    else:
        return 'Unidade de velocidade inválida';

velocidade = float(input('Digite a velocidade: '));
unitVelocidade = input('Digite a unidade de velocidade KM/H ou M/S (K ou M): ');
unitConvert = input('Digite a unidade de conversão KM/H ou M/S (K ou M): ');
print('A velocidade convertida é: ', converterVelocidade(velocidade, unitVelocidade, unitConvert));

# Descrição Função para converter distância de KM para Milhas ou de Milhas para KM
def converterDistancias (distancia, unitDistancia, unitConvert):
    if unitDistancia == 'M' and unitConvert == 'K' :
        return distancia * 1.61;
    elif unitDistancia == 'K' and unitConvert == 'M':
        return distancia / 1.61;
    else :
        return 'Unidade de Distância Inválida';

distancia = float(input('Digite a Distância: '));
unitDistancia = input('Digite a unidade de distância Quilômetros (K) ou Milhas (M): ');
unitConvert = input('Digite a unidade de conversão Quilômetros(K) ou Milhas(M): ');
print('A distância convertida é: ', converterDistancias(distancia, unitDistancia, unitConvert));