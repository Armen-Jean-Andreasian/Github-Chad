class InputTakerBase:
    @staticmethod
    def take_input(msg: str, return_type: type):
        user_input = input(msg).strip()

        try:
            return_type(user_input)
        except ValueError:
            raise ValueError(f"Provide '{return_type.__name__}' value!")
        else:
            return user_input


class Input:
    """Simple user input taker providing string and int input basic checks on given input"""

    @staticmethod
    def take_str(msg: str,
                 starts_with: str = None,
                 ends_with: str = None,
                 to_lower: bool = False,
                 contains: str = None) -> str:

        user_input = InputTakerBase.take_input(msg=msg, return_type=str)

        # checks
        if starts_with:
            if not user_input.startswith(starts_with):
                raise f"Should begin with {starts_with}"
        if ends_with:
            if not user_input.endswith(ends_with):
                raise f"Should end with {ends_with}"
        if contains:
            if contains not in user_input:
                raise f"Should contain {contains}"

        if to_lower:
            return user_input.lower()
        return user_input

    @staticmethod
    def take_int(msg: str) -> int:
        user_input = int(InputTakerBase.take_input(msg=msg, return_type=int))
        return user_input
