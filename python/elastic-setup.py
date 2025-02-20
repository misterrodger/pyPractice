from elasticsearch import Elasticsearch

client = Elasticsearch("http://localhost:9200")

index_name = "test-index"


def create_index():
    mapping = {
        "mappings": {
            "properties": {
                "name": {"type": "text"},
                "age": {"type": "integer"},
                "location": {"type": "text"},
            }
        }
    }

    client.indices.create(index=index_name, body=mapping)


def seed_data():
    data = [
        {"name": "Steve", "age": 25, "location": "Anywhere, USA"},
        {"name": "James", "age": 45, "location": "Chicago, USA"},
        {"name": "Jill", "age": 35, "location": "Paris, France"},
    ]

    for i, doc in enumerate(data):
        client.index(index=index_name, id=i + 1, document=doc)


if __name__ == "__main__":
    create_index()
    seed_data()
