
def email_builder(domain):
    def email_build(username):
        return f"{username}@{domain}"
    return email_build

email = email_builder("gmail.com")
hotinger=email_builder("hotinger.com")

print(email("perumal"))
print(hotinger("pichai"))



def email_build(username):
    return  f"{username}@gmail.com"
def hoster_email(username):
    return f"{username}@hoster.com"

def build_over_all(username,domain):
    return domain(username)

print(build_over_all("bala",email_build))
print(build_over_all("murugan",hoster_email))


def add_result(sum):

    def inner_add(a,b):
        return sum(a,b)
    return inner_add

def sum(a,b):
    return a+b
result = add_result(sum)

print(result(5,10))  # Output: 15
