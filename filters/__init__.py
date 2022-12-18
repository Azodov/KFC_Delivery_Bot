from loader import dp
from .admins import IsSuperAdmin
from .users import IsUser, IsGuest

if __name__ == "filters":
    dp.filters_factory.bind(IsSuperAdmin)
    dp.filters_factory.bind(IsUser)
    dp.filters_factory.bind(IsGuest)
