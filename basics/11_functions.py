def take_n_number_args(*args, **kwargs):
    print(args)
    print(kwargs)


take_n_number_args(4, 4, "ff", [2, 2, 3], (1, 2, 3), keyword_arg_1="dfdfd")
