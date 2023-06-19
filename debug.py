# output_flag = True
output_flag = False


def dbgprint(*args, **kwargs):
    if output_flag:
        print(*args, **kwargs)
