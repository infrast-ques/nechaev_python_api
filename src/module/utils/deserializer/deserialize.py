import marshmallow_dataclass
import typing_extensions


@typing_extensions.deprecated('use pydantic BaseModel(**dict)')
def __deserialize(class_type: type, dict_data: dict):
    class_instance = marshmallow_dataclass.class_schema(class_type)()
    return class_instance.load(data=dict_data)


@typing_extensions.deprecated('use pydantic model_dump_json()')
def __serialize(obj: object) -> dict:
    def apply_dict_recursive(_obj):
        if isinstance(_obj, dict):
            return {key: apply_dict_recursive(value) for key, value in _obj.items()}
        elif isinstance(_obj, list) or isinstance(_obj, tuple):
            return [apply_dict_recursive(item) for item in _obj]
        elif hasattr(_obj, '__dict__'):
            return apply_dict_recursive(_obj.__dict__)
        else:
            return _obj

    return apply_dict_recursive(obj)
