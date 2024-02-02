from Server.db_manager import base_manager
from Server.violator.models import (Violators, New_violator)
from Server.models.models import New_ID


def get_violators():
    res = base_manager.execute("SELECT Vr.id "
                               "FROM Violator Vr"
                               "INNER JOIN Visitor V ON Vr.visitor_id = V.id", many=True)
    violator = []
    for violator in res['data']:
        print()
        violator.append(Violators(id=violator[0], visitor_id=violator[1]))

    return violator

def get_violator(violator_id: int):
        res = base_manager.execute("SELECT V.id, V.visitor_id "
                                   "FROM Violator V WHERE id = ? ",
                                   args=(violator_id,))
        print(res)
        return Violators(id=violator_id, visitor_id=res['data'][0][1])

def add_new_violator(new_violator: New_violator):
    res = base_manager.execute("INSERT INTO Violator(visitor_id) "
                               "VALUES (?) "
                               "RETURNING id", args=(new_violator.visiotr_id))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_violator(violator_id: int, violator: New_violator):
    res = base_manager.execute("UPDATE Violator SET visitor_id = ? WHERE id = ? ",
                               args=(violator.visitor_id,  violator_id))
    return New_ID(code=res['code'], id=violator_id)

def delete_violator(violator_id: int):
    res = base_manager.execute("DELETE FROM Violator WHERE id = ?",
                               args=(violator_id, ))
    return New_ID(code=res['code'], id=violator_id)