from typing import List
from fastapi import APIRouter
from Server.models.models import New_ID
from Server.violator.models import (Violators, New_violator)
from Server.violator.resolvers import (get_violator, get_violators,
                                          add_new_violator, update_violator,
                                          delete_violator)


router = APIRouter()

@router.get('/', tags=["Violator"])
def router_violators() -> List[Violators]:
    return get_violators()

@router.get('/{violator_id}', tags=["Violator"])
def router_violator(violator_id: int) -> Violators:
    return get_violator(violator_id)

@router.post('/', tags=["Violator"])
def router_new_violator(new_violator: New_violator) -> New_ID:
    return add_new_violator(new_violator)

@router.put('/{violator_id}', tags=["Violator"])
def router_update_violator(violator_id: int, new_violator: New_violator) -> New_ID:
    return update_violator(violator_id, new_violator)

@router.delete('/{violator_id}', tags=["Violator"])
def router_delete_violator(id: int) -> New_ID:
    return delete_violator(id)