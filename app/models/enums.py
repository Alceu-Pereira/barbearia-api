from enum import Enum

class StatusAgendamento(str, Enum):
    AGENDADO = "AGENDADO"
    CONCLUIDO = "CONCLUIDO"
    CANCELADO = "CANCELADO"
    FALTOU = "FALTOU"