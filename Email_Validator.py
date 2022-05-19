class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def is_domain_invalid(domain, valid_domains):
    result = True
    for valid_domain in valid_domains:
        if domain.endswith(valid_domain):
            result = False
            break
    return result


valid_domains = [".com", ".bg", ".net", ".org"]
email = input()
while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    username, domain = email.split("@")
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if is_domain_invalid(domain, valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    email = input()
