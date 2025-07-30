def generate(numRows):
    result = [[1]]

    for _ in range(1, numRows):  # для каждой новой строки
        prev = result[-1]        # берем последнюю строку
        new_row = [1]            # начинаем новую строку с 1

        for i in range(len(prev) - 1):
            sum_val = prev[i] + prev[i + 1]
            new_row.append(sum_val)

        new_row.append(1)        # заканчиваем новую строку единицей
        result.append(new_row)   # добавляем в результат

    return result

print(generate(5))

