def check_string_characters(s):
    has_alphanumeric = any(c.isalnum() for c in s)
    has_alphabetical = any(c.isalpha() for c in s)
    has_digits = any(c.isdigit() for c in s)
    has_lowercase = any(c.islower() for c in s)
    has_uppercase = any(c.isupper() for c in s)

    return has_alphanumeric, has_alphabetical, has_digits, has_lowercase, has_uppercase

if __name__ == '__main__':
    s = input().strip()
    results = check_string_characters(s)

    for result in results:
        print(result)
