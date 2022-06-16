class NullElementException(Exception):
    def __init__(self, *args, **kwargs):
        default_message = "Invalid value provided for insertion!"

        if args:
            super().__init__(*args, **kwargs)
        else:
            super().__init__(default_message, **kwargs)


class EmptyStackException(Exception):
    def __init__(self, *args, **kwargs):
        default_message = "Stack is empty rightnow!"

        if args:
            super().__init__(*args, **kwargs)
        else:
            super().__init__(default_message, **kwargs)
