from typing import List, Optional
from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    icon: str
    path: str
    order_index: int
    level: int
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(MenuItemBase):
    pass

class MenuItem(MenuItemBase):
    id: int
    children: List['MenuItem'] = []

    class Config:
        from_attributes = True