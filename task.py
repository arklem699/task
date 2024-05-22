# Рекурсивная функция
def generate_expressions(nums, target, current_expr="", current_sum=0, prev_num=0):
    if not nums:
        if current_sum == target:
            print(f"{current_expr} = {target}")
        return

    next_num = nums[0]
    remaining_nums = nums[1:]

    # Сложение
    generate_expressions(
        remaining_nums, target,
        current_expr + f" + {next_num}",
        current_sum + next_num,
        next_num
    )

    # Вычитание
    generate_expressions(
        remaining_nums, target,
        current_expr + f" - {next_num}",
        current_sum - next_num,
        -next_num
    )

    # Конкатенация
    if current_expr:
        new_num = abs(prev_num) * 10 + next_num
        if prev_num > 0:
            new_sum = current_sum - prev_num + new_num
        else:
            new_sum = current_sum - prev_num - new_num
        generate_expressions(
            remaining_nums, target,
            current_expr + f"{next_num}",
            new_sum,
            prev_num // abs(prev_num) * new_num
        )


def find_expressions():
    nums = list(range(9, -1, -1))  # [9, 8, ..., 0]
    target = 200
    for i in range(1, len(nums)):
        generate_expressions(nums[i:], target, str(nums[0]), nums[0], nums[0])


if __name__ == '__main__':
    find_expressions()