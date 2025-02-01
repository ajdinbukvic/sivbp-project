from faker import Faker
import random

fake = Faker()

def generate_fake_documents(count):
    docs = []
    for _ in range(count):
        doc = {
            "abstract": fake.text(max_nb_chars=500),
            "authors": fake.name(),
            "authors_parsed": [{"affiliation": fake.company(), "name": fake.first_name(), "surname": fake.last_name()}],
            "categories": random.choice(["cs.AI", "cs.LG", "math.ST", "physics.optics"]),
            "comments": fake.text(max_nb_chars=200),
            "content": fake.text(max_nb_chars=random.randint(1000, 5000)),
            "doi": fake.uuid4(),
            "id": fake.uuid4(),
            "journal-ref": fake.sentence(),
            "journal_ref": fake.sentence(),
            "license": random.choice(["arXiv", "CC BY", "MIT"]),
            "report-no": fake.uuid4(),
            "report_no": fake.uuid4(),
            "submitter": fake.name(),
            "title": fake.sentence(nb_words=random.randint(3, 10)),
            "update_date": fake.date(),
            "versions": [{"created": fake.date(), "version": str(random.randint(1, 10))}]
        }
        docs.append(doc)
    return docs
