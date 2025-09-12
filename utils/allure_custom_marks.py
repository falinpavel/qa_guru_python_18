import allure

from functools import wraps


def allure_high_level_marks(epic: str, feature: str):
    def class_decorator(cls):
        cls = allure.epic(epic)(cls)
        cls = allure.feature(feature)(cls)
        return cls
    return class_decorator


def allure_mid_level_marks(story: str, testcase_id: str, title: str, label: str, owner: str):
    def func_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            allure.dynamic.story(story)
            allure.dynamic.testcase(testcase_id)
            allure.dynamic.title(title)
            allure.dynamic.label(label)
            allure.dynamic.label("owner", owner)
            return func(*args, **kwargs)
        return wrapper
    return func_decorator
