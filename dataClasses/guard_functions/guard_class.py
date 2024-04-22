def is_sub_class(value: any, class_type: type) -> bool:
    if value is None:
        return False
    _type = type(value)
    return issubclass(_type, class_type)