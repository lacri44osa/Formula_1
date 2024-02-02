from Server.db_manager import base_manager
from Server.visitors.models import (Visitors, New_visitor, Certain_visitor, Update_visitor)
from Server.models.models import New_ID


def get_visitors():
    res = base_manager.execute("SELECT V.id, V.name, V.surname, V.middle_name, V.ticket_number, V.ticket_price, V.seat_number "
                               "FROM Visitor V ", many=True)
    visitors = []
    for visitor in res['data']:
        print()
        visitors.append(Visitors(id=visitor[0], name=visitor[1], surname=visitor[2],
                                         middle_name=visitor[3], ticket_number=visitor[4], ticket_price=visitor[5], seat_number=visitor[6]))
    return visitors

def get_visitor(visitor_id: int):
    res = base_manager.execute("SELECT V.id, V.name, V.surname, V.seat_number "
                               "FROM Visitor V WHERE id = ? ",
                               args=(visitor_id, ))
    print(res)
    return Certain_visitor(id=visitor_id, name=res['data'][0][1], surname=res['data'][0][2], seat_number=res['data'][0][3])

def add_new_visitor(new_visitor: New_visitor):
    res = base_manager.execute("INSERT INTO Visitor(name, surname, middle_name, ticket_number, ticket_price, seat_number) "
                               "VALUES (?, ?, ?, ?, ?, ?) "
                               "RETURNING id", args=(new_visitor.name, new_visitor.surname, new_visitor.middle_name,
                                                     new_visitor.ticket_number, new_visitor.ticket_price, new_visitor.seat_number))
    return New_ID(code=res['code'], id=res['data'][0][0])

def update_visitor(visitor_id: int, visitor: Update_visitor):
    res = base_manager.execute("UPDATE Visitor SET name = ?, surname = ?, middle_name = ? WHERE id = ? ",
                               args=(visitor.name, visitor.surname, visitor.middle_name, visitor_id, ))
    return New_ID(code=res['code'], id=visitor_id)

def delete_visitor(visitor_id: int):
    res = base_manager.execute("DELETE FROM Visitor WHERE id = ?",
                               args=(visitor_id,))
    return New_ID(id=visitor_id, code=res['code'])