def put_my_args_types(*args):
    for key, arg in enumerate(args):
        print( 'Argument {0} is an {1} \n'.format(arg, type(arg).__name__) )