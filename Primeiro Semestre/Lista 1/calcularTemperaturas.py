# Descrição: Função que converte temperaturas de Celsius para Fahrenheit, Fahrenheit para Celsius, Celsius para Kelvin e Kelvin para Celsius.
def converter(temperature, unitTemperature, unitConvert):
    if unitTemperature == 'C' and unitConvert == 'F':
        return 9 * temperature / 5 + 32;
    elif unitTemperature == 'F' and unitConvert == 'C':
        return 5 * (temperature - 32) / 9;
    elif unitTemperature == 'C' and unitConvert == 'K':
        return temperature - 273.15;
    elif unitTemperature == 'K' and unitConvert == 'C':
        return temperature + 273.15;
    else:
        return 'Unidade de temperatura inválida';

temperature = float(input('Digite a temperatura: '));
unitTemperature = input('Digite a unidade de temperatura (C, F ou K): ');
unitConvert = input('Digite a unidade de conversão (C, F ou K): ');

print('A temperatura convertida é: ', converter(temperature, unitTemperature, unitConvert));
