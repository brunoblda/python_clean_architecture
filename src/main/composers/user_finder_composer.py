from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_finder import UserFinder
from src.presentation.controllers.user_finder_controller import UserFinderController


def user_finder_composer():
    users_repository = UsersRepository()
    user_finder_use_case = UserFinder(users_repository)
    user_finder_controller = UserFinderController(user_finder_use_case)

    return user_finder_controller.handle
