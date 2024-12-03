from operator import itemgetter


class Syntax:
    def __init__(self, id, name, lang_id):
        self.id = id
        self.name = name
        self.lang_id = lang_id


class Language:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SyntaxLang:
    def __init__(self, lang_id, syntax_id):
        self.lang_id = lang_id
        self.syntax_id = syntax_id


def one_to_many_relationship(languages, syntaxes):
    return [(s.name, l.name) for l in languages for s in syntaxes if s.lang_id == l.id]


def many_to_many_relationship(languages, syntaxes, syntaxes_langs):
    many_to_many_temp = [(l.name, sl.lang_id, sl.syntax_id)
                         for l in languages for sl in syntaxes_langs if l.id == sl.lang_id]
    return [(s.name, l_name) for l_name, _, syntax_id in many_to_many_temp for s in syntaxes if s.id == syntax_id]


def task_v1_python_syntax(one_to_many):
    return [name for name, lang in one_to_many if lang == 'Python']


def task_v2_min_syntax(languages, one_to_many):
    res_2_unsorted = []
    for l in languages:
        l_syntaxes = list(filter(lambda x: x[1] == l.name, one_to_many))
        if l_syntaxes:
            min_syntax = min([syntax for syntax, _ in l_syntaxes])
            res_2_unsorted.append((l.name, min_syntax))
    return sorted(res_2_unsorted, key=lambda x: x[1])


def task_v3_syntax_language(many_to_many):
    return sorted(many_to_many, key=lambda x: x[0])
