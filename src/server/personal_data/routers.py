from typing import List
from fastapi import APIRouter
from personal_data.models import Personal_data
from personal_data.resolvers import get_personal_data

router = APIRouter()

@router.get('/')
def get_all_personal_data() -> List[Personal_data]:
    return get_personal_data()