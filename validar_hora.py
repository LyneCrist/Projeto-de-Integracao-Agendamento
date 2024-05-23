from datetime import datetime, time

start_time = time(8, 0, 0)
end_time = time(17, 0, 0)

hora_consulta = time(17, 1, 0)

if hora_consulta < start_time or hora_consulta > end_time:

    print(
        "Erro: Hora informada deve respeitar janela de atendimento, das 08hrs às 17hrs"
    )
