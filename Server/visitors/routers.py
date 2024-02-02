from typing import List
from fastapi import APIRouter
from Server.visitors.models import (Visitors, New_visitor,
                                   Certain_visitor, Update_visitor)
from Server.visitors.resolvers import (get_visitors, get_visitor,
                                      add_new_visitor, update_visitor, delete_visitor)
from Server.models.models import New_ID

router = APIRouter()


@router.get('/', tags=["visitors"])
def router_visitors() -> List[Visitors]:
    return get_visitors()

@router.get('/{visitor_id}', tags=["visitors"])
def router_certain_visitor(visitor_id: int) -> Certain_visitor:
    return get_visitor(visitor_id)

@router.post('/', tags=["visitors"])
def router_new_client(new_visitor: New_visitor) -> New_ID:
    return add_new_visitor(new_visitor)

@router.put('/{visitor_id}', tags=["visitors"])
def router_update_visitor(visitor_id: int, new_visitor: Update_visitor) -> New_ID:
    return update_visitor(visitor_id, new_visitor)

@router.delete('/{visitor_id}', tags=["visitors"])
def router_delete_visiotr(id: int) -> New_ID:
    return delete_visitor(id)