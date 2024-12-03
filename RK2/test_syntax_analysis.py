import unittest
from syntax_analysis import (
    Language, Syntax, SyntaxLang, 
    one_to_many_relationship, many_to_many_relationship, 
    task_v1_python_syntax, task_v2_min_syntax, task_v3_syntax_language
)


class TestSyntaxAnalysis(unittest.TestCase):
    def setUp(self):
        self.languages = [
            Language(1, 'Python'),
            Language(2, 'C++'),
            Language(3, 'JavaScript'),
        ]

        self.syntaxes = [
            Syntax(1, 'Цикл for', 1),
            Syntax(2, 'Условие if', 2),
            Syntax(3, 'Функция', 1),
            Syntax(4, 'Объект', 3),
            Syntax(5, 'Массив', 2),
        ]

        self.syntaxes_langs = [
            SyntaxLang(1, 1),
            SyntaxLang(1, 3),
            SyntaxLang(2, 2),
            SyntaxLang(2, 5),
            SyntaxLang(3, 4),
        ]

    def test_task_v1(self):
        one_to_many = one_to_many_relationship(self.languages, self.syntaxes)
        result = task_v1_python_syntax(one_to_many)
        self.assertEqual(result, ['Цикл for', 'Функция'])

    def test_task_v2(self):
        one_to_many = one_to_many_relationship(self.languages, self.syntaxes)
        result = task_v2_min_syntax(self.languages, one_to_many)
        self.assertEqual(result, [('C++', 'Массив'), ('JavaScript', 'Объект'), ('Python', 'Функция')])

    def test_task_v3(self):
        many_to_many = many_to_many_relationship(self.languages, self.syntaxes, self.syntaxes_langs)
        result = task_v3_syntax_language(many_to_many)
        self.assertEqual(result, [
        ('Массив', 'C++'),
        ('Объект', 'JavaScript'),
        ('Условие if', 'C++'),
        ('Функция', 'Python'),
        ('Цикл for', 'Python'),
    ])



if __name__ == '__main__':
    unittest.main()
