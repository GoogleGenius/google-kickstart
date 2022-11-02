def calculate(
    total_animals: int,
    dog_portions: int,
    cat_portions: int,
    extra_cat_portions: int,
    order: str,
) -> bool:
    if total_animals != len(order):
        raise ValueError("`total_animals` does not match len `order`")

    order_list = list(order)

    for animal in order_list.copy():
        if animal == "D" and not dog_portions:
            return False
        if animal == "C" and not cat_portions and "D" in order_list:
            return False
        if animal == "D":
            order_list.remove("D")
            dog_portions -= 1
            cat_portions += extra_cat_portions
        else:
            order_list.remove("C")
            cat_portions -= 1

    return True


def parse_input() -> list[bool]:
    case_number = int(input())
    result_data: list[bool] = []
    parsed_numbers: list[int] = []
    order_string: str = ""

    while len(result_data) != case_number:
        console_input = input()

        if "D" in console_input or "C" in console_input:
            order_string = console_input
        else:
            parsed_numbers = [int(number) for number in console_input.split()]

        if parsed_numbers and order_string:
            result_data.append(
                calculate(
                    total_animals=parsed_numbers[0],
                    dog_portions=parsed_numbers[1],
                    cat_portions=parsed_numbers[2],
                    extra_cat_portions=parsed_numbers[3],
                    order=order_string,
                )
            )

            parsed_numbers = []
            order_string = ""

    return result_data


def generate_output(result_data: list[bool]) -> str:
    leading_string = "Case #"

    return "\n".join(
        f"{leading_string}{count + 1}: {'YES' if case else 'NO'}"
        for count, case in enumerate(result_data)
    )


def main() -> None:
    print(generate_output(parse_input()))


if __name__ == "__main__":
    main()
