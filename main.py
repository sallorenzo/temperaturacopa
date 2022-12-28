import requests
import json
from datetime import date
from datetime import datetime, timedelta
from time import time


def buscar_dados(ts_ontem, ts_hoje):
    request = requests.get(
        f"https://simcosta.furg.br/api/oceanic_data?boiaID=12&type=json&time1={ts_ontem}&time2={ts_hoje}&params=Average_Temperature_C")

    data_dict = json.loads(request.content)

    dataHoraontem = datetime.now()- timedelta(1)
    dataHoraHoje = datetime.now()

    ##print(data_dict[0])
    ##print(data_dict[-1])


    print("Temperatura ontem às", dataHoraontem.strftime('%H:%M'),":",data_dict[0]["Avg_W_Tmp2"])
    print("Temperatura ontem às", dataHoraHoje.strftime('%H:%M'),":",data_dict[-1]["Avg_W_Tmp2"])



dia_ontem = datetime.now() - timedelta(1)
ts_ontem = datetime.timestamp(dia_ontem)


dia_hoje = datetime.now()
ts_hoje = datetime.timestamp(dia_hoje)


buscar_dados(ts_ontem, ts_hoje)


