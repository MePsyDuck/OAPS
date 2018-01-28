from django_seed import Seed

from api.models import User, Letter, Remark

seeder = Seed.seeder()

seeder.add_entity(User, 20, {
    'password': lambda x: seeder.faker.password(length=6, special_chars=False, digits=False, upper_case=False,
                                                lower_case=True),
    'is_superuser': lambda x: False,
    'username': lambda x: seeder.faker.user_name(),
    'first_name': lambda x: seeder.faker.first_name(),
    'last_name': lambda x: seeder.faker.last_name(),
    'email': lambda x: seeder.faker.email(),
    'is_staff': lambda x: seeder.faker.pybool(),
    'is_active': lambda x: seeder.faker.pybool(),
    'acc_type': lambda x: seeder.faker.random_int(min=0, max=1)
})

seeder.add_entity(Letter, 20, {
    'body': lambda x: seeder.faker.paragraphs(nb=3),
    'subject': lambda x: seeder.faker.sentence(nb_words=6),
})

seeder.add_entity(Remark, 20, {
    'action': lambda x: seeder.faker.random_int(min=0, max=2),
    'message': lambda x: seeder.faker.sentence(nb_words=8),
})

inserted_pks = seeder.execute()

print(inserted_pks)
