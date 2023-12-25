from db_manager import db_manager
from personal_data.models import Personal_data, Certain_personal_data, New_personal_data, Update_personal_data

def get_personal_data():
    res = db_manager.execute("SELECT pd.passport_number, pd.passport_organ, pd.passport_date, pd.snils"
                             "pd.phone_number FROM personal_data ", many=True)
    personal_data = []
    for pd in res['data']:
        print()
        personal_data.append(Personal_data(passport_number=pd[0], passport_organ=pd[1], passport_date=pd[2], snils=pd[3], phone_number=pd[4]))
    return personal_data