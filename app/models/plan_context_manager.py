

class Plan_context_manager:
    #con el __ imitamos el private
    def __init__(self):
        self.__user_context = {}
        self.__plan_context = {}
        self.__usage_limits_context = {}

    def get_user_context(self) -> dict:
        return self.__user_context

    def set_user_context(self, user_context: dict):
        self.__user_context = user_context

    def get_plan_context(self) -> dict:
        return self.__plan_context

    def set_plan_context(self, plan_context: dict):
        self.__plan_context = plan_context

    def get_usage_limits_context(self) -> dict:
        return self.__usage_limits_context

    def set_usage_limits_context(self, usage_limits_context: dict):
        self.__usage_limits_context = usage_limits_context
