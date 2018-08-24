def validate_my_parameters(int_required, str_required, float_required, *args):
    return (
        int_required == [isinstance(arg, int) for arg in args].count(True),
        str_required == [isinstance(arg, str) for arg in args].count(True),
        float_required == [isinstance(arg, float) for arg in args].count(True)
    )
