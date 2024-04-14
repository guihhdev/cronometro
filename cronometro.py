import time
import keyboard

def cronometro():
    # Inicializa a variável 'inicio' como None (ainda não começou o cronômetro)
    print("Cronômetro. Pressione Q para começar.")
    inicio = None
    while True:
        # Verifica se a tecla 'q' foi pressionada e se o cronômetro ainda não começou
        if keyboard.is_pressed('q') and not inicio:
            # Captura o tempo atual como início do cronômetro
            inicio = time.time()
            print("Cronômetro iniciado. Pressione 'r' para encerrar.")
        # Verifica se a tecla 'r' foi pressionada e se o cronômetro já começou
        elif keyboard.is_pressed('r') and inicio:
            # Calcula a duração total do cronômetro
            tempo = time.time() - inicio
            print(f"Cronômetro encerrado. Tempo total: {tempo} segundos")
            espaco = float(input("Apague o texto do terminal em seguida-> Digite qual é o espaço (em metros): "))
            velocidade = espaco / tempo
            print(f"Velocidade média: {velocidade} m/s")
            break

# Chama a função para iniciar o cronômetro
cronometro()

