import schedule
import time

def tarefa():
    print("teste")

# schedule.every(5).weeks.do(tarefa) -> Rodar de 5 em 5 semanas
# schedule.every().day.at("14:28").do(tarefa) -> Rodar todos os dias ás 14h28m
# schedule.every().wednesday.at("14:31").do(tarefa) -> Rodar toda quarta-feira ás 14h31m
# schedule.every().hour.at(":30").do(tarefa) -> Rodar á cada hora no minuto 30. Ex: 10h30m, 11h30m, 12h30m etc...
# schedule.every().second.until("14:36").do(tarefa) -> Rodar a cada segundo até o horário ser 14h36m

while True:
    schedule.run_pending()
    time.sleep(1)