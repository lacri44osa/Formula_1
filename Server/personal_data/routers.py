from typing import List
from fastapi import APIRouter
from Server.personal_data.models import Personal_data, Certain_personal_data, New_personal_data, Update_personal_data
from Server.personal_data.resolvers import (get_personal_data, get_personals_data, add_new_personal_data, update_personal_data, delete_personal_data)
from Server.models.models import New_ID

router = APIRouter()


@router.get('/', tags=["personal_data"])
def router_personal_data() -> List[Personal_data]:
    return get_personals_data()

@router.get('/{personal_data_id}', tags=["personal_data"])
def router_certain_personal_data(cat_id: int) -> Certain_personal_data:
    return get_personal_data(cat_id)

@router.post('/', tags=["personal_data"])
def router_new_personal_data(new_pd: New_personal_data) -> New_ID:
    return add_new_personal_data(new_pd)

@router.put('/{personal_data_id}', tags=["personal_data"])
def router_update_personal_data(pd_id: int, new_client: Update_personal_data) -> New_ID:
    return update_personal_data(pd_id, new_client)

@router.delete('/{personal_data_id}', tags=["personal_data"])
def router_delete_personal_data(id: int) -> New_ID:
    return delete_personal_data(id)