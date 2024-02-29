def calcularAngulo(angulo, unit, unitConvert):
    if unit == 'G' and unitConvert == 'R':
        return angulo * 3.14/180;
    elif unit == 'R' and unitConvert == 'G':
        return angulo * 180/3.14;
    else :
        return 'Operação Inválida';

angulo = float(input("Digite um Ângulo: "));
unit = input("Escolha a unidade do Ângulo (G ou R): ");
unitConvert = input("Escolha a unidade de conversão (G ou R): ");
print("O Ângulo convertido é: ", calcularAngulo(angulo, unit, unitConvert));