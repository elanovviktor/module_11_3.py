def  introspection_info(obj):
    obj_type = type (obj).__name__# определяеь тип обьекта

    attributes = dir (obj)#определяем атрибуты щбьекта

    methods = [method for method in attributes if callable(getattr(obj, method))]#методы обьекта

    module = obj.__class__.__module__#определение Модуля, к которому объект принадлежит

    info = {'tupe' : obj_type,'attributes': attributes,'methods': methods, 'module': module }# информация об обьекте

    return info
number_info = introspection_info(42)
print(number_info)
string_info = introspection_info('Привет')
print(string_info)
list_info = introspection_info([10,20,30, 'word'])
print(list_info)
