# Programa para converter medida em Centímetros para Polegadas e vice-versa
def converterCP (medida, unit, unitConvert):
    if unit == 'P' and unitConvert == 'C':
        return medida * 2.54;
    elif unit == 'C' and unitConvert == 'P':
        return medida / 2.54;
    else :
        return 'Medida Inserida Inválida';

medida = float(input('Insira a Medida a ser Convertida: '));
unit = input('Insira a unidade de medida : Centímetros(C) ou Polegadas(P)');
unitConvert = input('Insira a unidade de media para ser convertida: Centímetros(C) ou Polegadas(P)');

print('A medida convertida é ', converterCP(medida, unit, unitConvert));

# Programa par converter Volume de Metros Cúbicos para Litros e vice-versa
def converterVolume (medida, unit, unitConvert):
    if unit == 'M' and unitConvert == 'L':
        return 1000 * medida;
    elif unit == 'L' and unitConvert == 'M':
        return medida / 1000 ;
    else : 
        return 'Erro! Medida Inserida Inválida.';

medida = float(input('Insira a Medida a ser Convertida: '));
unit = input('Insira a unidade de medida : Metros Cúbicos(M) ou Litros(L) ->');
unitConvert = input('Insira a unidade de medida para ser convertida: Metros Cúbicos(M) ou Litros(L) -> ');

print('A medida convertida é ', converterVolume(medida, unit, unitConvert));

# Programa para converter massa, de quilograma para libras e vice-versa
def converterMassa(medida, unit, unitConvert):
    if unit == 'K' and unitConvert == 'L':
        return medida / 0.45;
    elif unit == 'L' and unitConvert == 'K':
        return medida * 0.45;
    else :
        return 'Erro! Medida Inserida Inválida.';

medida = float(input('Insira a Medida a ser Convertida: '));
unit = input('Insira a unidade de medida : Quilogramas(K) ou Libras(L) ->'); 
unitConvert = input('Insira a unidade de medida para ser convertida: Quilogramas(K) ou Libras(L) -> ');

print('A medida convertida é ', converterMassa(medida, unit, unitConvert));

# Programa para converter comprimento, de metros para jardas e vice-versa
def converterComprimento(medida, unit, unitConvert):
    if unit == 'M' and unitConvert == 'J':
        return medida / 0.91;
    elif unit == 'J' and unitConvert == 'M':
        return medida * 0.91;
    else :
        return 'Erro! Medida Inserida Inválida.';
medida = float(input('Insira a Medida a ser Convertida: '));
unit = input('Insira a unidade de medida : Metros(M) ou Jardas(J) ->');
unitConvert = input('Insira a unidade de medida para ser convertida: Metros(M) ou Jardas(J) -> ');

print('A medida convertida é ', converterComprimento(medida, unit, unitConvert));

# Programa para converter medidas de área
def converterArea(medida, unit, unitConvert):
    if unit == 'M' and unitConvert == 'A':
        return medida * 0.000247;
    elif unit == 'A' and unitConvert == 'M':
        return medida * 4048.58;
    elif unit == 'M' and unitConvert == 'H':
        return medida * 0.0001;
    elif unit == 'H' and unitConvert == 'A':
        return medida * 10000;
    else :
        return 'Medida Inválida';

medida = float(input('Digite o valor da área: '));
unit = input('Digite a unidade de área entre Metros Quadrados(M), Acres(A) ou Hectares(H): ');
unitConvert = input('Digite unidade de conversão entre Metros Quadrados(M), Acres(A) ou Hectares(H): ');
print('A área convertida é: ', converterArea(medida, unit, unitConvert));