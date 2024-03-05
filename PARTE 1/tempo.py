# Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos
segundos = int(input('Digite um valor em segundos: '));
horas = segundos // 3600;
minutos = segundos // 60;
print(horas, 'horas,', minutos, 'minutos e', segundos, 'segundos.');

# Faça um programa para ler o horário (hora, minuto e segundo) de início e a duração, em segundos, de uma experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.
hora = int(input('Digite a hora de início: '));
minuto = int(input('Digite o minuto de início: '));
segundo = int(input('Digite o segundo de início: '));
duracao = int(input('Digite a duração da experiência em segundos: '));
segundo = segundo + duracao;
minuto = minuto + segundo // 60;
hora = hora + minuto // 60;
segundo = segundo % 60;
minuto = minuto % 60;
hora = hora % 24;
print(hora, 'horas,', minuto, 'minutos e', segundo, 'segundos.'); 

# Calcular o ano de nascimento de uma pessoa a partir de sua idade e do ano atual
import datetime;
idade = int(input('Digite a idade da pessoa: '));
ano_atual = datetime.datetime.now().year;
ano_nascimento = ano_atual - idade;
print('O ano de nascimento da pessoa é: ', ano_nascimento);