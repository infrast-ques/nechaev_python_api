import marshmallow_dataclass


def deserialize(class_type: type, dict_data: dict):
    class_instance = marshmallow_dataclass.class_schema(class_type)()
    return class_instance.load(data=dict_data)


def serialize(obj: object) -> dict:
    def apply_dict_recursive(_obj):
        if isinstance(_obj, dict):
            return {key: apply_dict_recursive(value) for key, value in _obj.items()}
        elif isinstance(_obj, list):
            return [apply_dict_recursive(item) for item in _obj]
        elif hasattr(_obj, '__dict__'):
            return apply_dict_recursive(_obj.__dict__)
        else:
            return _obj

    return apply_dict_recursive(obj)