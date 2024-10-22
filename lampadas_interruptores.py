class SalaLampadas:
    def __init__(self):
        self.lampada1 = False  # Lâmpada 1 inicialmente desligada
        self.lampada2 = False  # Lâmpada 2 inicialmente desligada
        self.lampada3 = False  # Lâmpada 3 inicialmente desligada
        self.temperatura1 = "fria"  # Lâmpada 1 começa fria
        self.temperatura2 = "fria"  # Lâmpada 2 começa fria
        self.temperatura3 = "fria"  # Lâmpada 3 começa fria
    
    def ligar_lampada(self, lampada, minutos):
        if lampada == 1:
            self.lampada1 = True
            if minutos > 0:
                self.temperatura1 = "quente"
        elif lampada == 2:
            self.lampada2 = True
            if minutos > 0:
                self.temperatura2 = "quente"
        elif lampada == 3:
            self.lampada3 = True
            if minutos > 0:
                self.temperatura3 = "quente"
    
    def desligar_lampada(self, lampada):
        if lampada == 1:
            self.lampada1 = False
        elif lampada == 2:
            self.lampada2 = False
        elif lampada == 3:
            self.lampada3 = False
    
    def verificar_lampadas(self):
        # Retorna o status das lâmpadas e suas temperaturas
        return {
            "lampada1": (self.lampada1, self.temperatura1),
            "lampada2": (self.lampada2, self.temperatura2),
            "lampada3": (self.lampada3, self.temperatura3),
        }

# Simulação
sala = SalaLampadas()

# Passo 1: Ligue o primeiro interruptor e deixe-o por alguns minutos (lampada 1 fica quente)
sala.ligar_lampada(1, 5)

# Passo 2: Desligue o primeiro interruptor e ligue o segundo (lampada 1 ficará quente, lampada 2 será ligada)
sala.desligar_lampada(1)
sala.ligar_lampada(2, 0)

# Passo 3: Vá até a sala das lâmpadas e verifique
resultado = sala.verificar_lampadas()

# Mostra o resultado final
for lampada, status in resultado.items():
    ligada, temperatura = status
    print(f"{lampada}: {'ligada' if ligada else 'desligada'}, {temperatura}")
