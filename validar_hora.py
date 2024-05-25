from datetime import datetime, time

# start_time = time(8, 0, 0)
# end_time = time(17, 0, 0)

# hora_consulta = time(17, 1, 0)

# if hora_consulta < start_time or hora_consulta > end_time:

#     print(
#         "Erro: Hora informada deve respeitar janela de atendimento, das 08hrs às 17hrs"
#     )


STATUS_CHOICES = ((1, "Agendado"), (2, "Cancelado"), (3, "Realizado"))

users = [("user-kb001", 2), ("user-kb045", 1), ("user-kb025", 3)]


def filter_status(data, status_choice):
    return (
        data[0],
        next(filter(lambda status: status[0] == data[1], status_choice)),
    )


result = list(map(lambda user: filter_status(user, STATUS_CHOICES), users))

print(result)
