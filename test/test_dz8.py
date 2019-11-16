import module.victory as victory


def test_count_victory_questions():
    assert victory.count_victory_questions("3") == 5, "Ошибка, если задано значение меньше 4, должно возвращаться 5"
    assert victory.count_victory_questions("4") == 4, "Ошибка, если задано значение меньше 4, должно возвращаться 4"
    assert victory.count_victory_questions("text") == 5, "Ошибка, если задано значение не число, должно возвращаться 5"
    assert victory.count_victory_questions(str(len(victory.fio_birth) -1)) == len(victory.fio_birth) -1, \
        "Ошибка, на максимальное значение в списке"
    assert victory.count_victory_questions("20") == 5, "Ошибка, если задано значение больше длины списка," \
                                                       " должно возвращаться 5"
