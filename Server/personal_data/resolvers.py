from datetime import datetime
from Server.db_manager import base_manager
from Server.personal_data.models import (Personal_data, Certain_personal_data, New_personal_data)
from Server.models.models import New_ID


def get_personals_data():
    res = base_manager.execute("SELECT pd.passport_number, pd.passport_organ, pd.passport_date, pd.snils"
                             "pd.phone_number FROM personal_data pd", many=True)
    personal_data = []
    for pd in res['data']:
        print()
        personal_data.append(Personal_data(passport_number=pd[0], passport_organ=pd[1], 
                                           passport_date=datetime.strptime(pd[2],'%Y-%m-%d %H:%M:%S.%f'), snils=pd[3], phone_number=pd[4]))
    return personal_data

def get_personal_data(personal_data_id: int):
    res = base_manager.execute("SELECT pd.passport_number, "
                             "pd.phone_number FROM personal_data pd WHERE id = ? ",
                               args=(personal_data_id, ))
    print(res)
    return Certain_personal_data(id=personal_data_id, passport_number=res['data'][0][1], phone_number=res['data'][0][2])

def add_new_personal_data(new_pd: New_personal_data):
    res = base_manager.execute("INSERT INTO Personal_data(passport_number, passport_organ, passport_date, snils, phone_number) "
                               "VALUES (?, ?, ?, ?, ?) "
                               "RETURNING id", args=(new_pd.passport_number, new_pd.passport_organ, new_pd.passport_date, new_pd.snils, new_pd.phone_number))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_personal_data(personal_data_id: int, personal_data: New_personal_data):
    res = base_manager.execute("UPDATE Personal_data SET phone_number = ? WHERE id = ? ",
                               args=(personal_data.name, personal_data.id, ))
    return New_ID(code=res['code'], id=personal_data_id)

def delete_personal_data(personal_data_id: int):
    res = base_manager.execute("DELETE FROM Personal_data WHERE id = ?",
                               args=(personal_data_id,))
    return New_ID(id=personal_data_id, code=res['code'])