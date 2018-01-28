from django_seed import Seed

from api.models import User, Letter, Remark

seeder = Seed.seeder()

COUNT = 20

with open("dummy_accounts.txt", mode='w') as f:
    f.write("Password : Email\n")


def username():
    uname = seeder.faker.user_name()
    with open('dummy_accounts.txt', mode='a+') as file:
        file.write(uname)
        file.write("\n")
    return uname


def password():
    pword = seeder.faker.password(length=6, special_chars=False, digits=False, upper_case=False, lower_case=True)
    with open('dummy_accounts.txt', mode='a+') as file:
        file.write(pword)
        file.write(" : ")
    from django.contrib.auth.hashers import make_password
    return make_password(pword)


seeder.add_entity(User, COUNT, {
    'is_superuser': lambda x: False,
    'username': lambda x: username(),
    'password': lambda x: password(),
    'first_name': lambda x: seeder.faker.first_name(),
    'last_name': lambda x: seeder.faker.last_name(),
    'email': lambda x: seeder.faker.email(),
    'is_staff': lambda x: seeder.faker.pybool(),
    'is_active': lambda x: True,
    'acc_type': lambda x: seeder.faker.random_int(min=0, max=1)
})

seeder.add_entity(Letter, COUNT, {
    'body': lambda x: seeder.faker.text(),
    'subject': lambda x: seeder.faker.sentence(nb_words=6),
})

seeder.add_entity(Remark, COUNT, {
    'action': lambda x: seeder.faker.random_int(min=0, max=2),
    'message': lambda x: seeder.faker.sentence(nb_words=8),
})

inserted_pks = seeder.execute()

print(inserted_pks)
