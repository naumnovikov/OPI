class ClientService:
    def authenticate(self, login, password):
        # Критический баг исправлен: добавлена проверка на пустой пароль
        if not login or not password:
            return False
        return True
