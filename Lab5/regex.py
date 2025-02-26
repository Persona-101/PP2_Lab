import re

def match_a_followed_by_b(string):
    return bool(re.fullmatch(r'a*b*', string))

def match_a_followed_by_two_three_b(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

def find_lowercase_with_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

def find_upper_followed_by_lower(string):
    return re.findall(r'[A-Z][a-z]+', string)

def match_a_anything_b(string):
    return bool(re.fullmatch(r'a.*b', string))

def replace_space_comma_dot(string):
    return re.sub(r'[ ,.]', ':', string)

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

def insert_spaces_between_capitals(string):
    return re.sub(r'([A-Z])', r' \1', string).strip()

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
