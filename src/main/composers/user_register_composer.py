from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_register import UserRegister
from src.presentation.controllers.user_register_controller import UserRegisterController


def user_register_composer():
    users_repository = UsersRepository()
    user_register_use_case = UserRegister(users_repository)
    user_register_controller = UserRegisterController(user_register_use_case)

    return user_register_controller.handle
