from models import *

l1 = Library()
authors = l1.get_all_authors()
for author in authors:
    print(author.id, author.name, author.family)

l1 = Library()
publishers = l1.get_all_publishers()
for publisher in publishers:
    print(publisher.id, publisher.name, publisher.address,
          publisher.phone_number, publisher.email)

l1 = Library()
genres = l1.get_all_genres()
for genre in genres:
    print(genre.id, genre.name)

l1 = Library()
designers = l1.get_all_designers()
for designer in designers:
    print(designer.id, designer.name, designer.family)

l1 = Library()
sources = l1.get_all_sources()
for source in sources:
    print(source.id, source.name, source.author_name)

l1 = Library()
translators = l1.get_all_translators()
for translator in translators:
    print(translator.id, translator.name, translator.family)


# a1 = Author(0, "ali", "rezaei")
# l1.insert_author(a1)

# a1 = Publisher(0, "ali", "-", "0", "-")
# l1.insert_publisher(a1)

# a1 = Genre(0, "ali")
# l1.insert_genre(a1)

# a1 = Designer(0, "ali", "rezaei")
# l1.insert_designer(a1)

# a1 = Source(0, "ali", "reza")
# l1.insert_source(a1)

# a1 = Translator(0, "ali", "rezaei")
# l1.insert_translator(a1)

# l1.delete_author(12)
# l1.delete_publisher(11)
# l1.delete_genre(6)
# l1.delete_designer(11)
# l1.delete_source(51)
# l1.delete_translator(11)

# a1 = Author(12, "alireza", "rezaei")
# l1.update_author(a1)

# a1 = Publisher(11, "alireza", "-", 0, "-")
# l1.update_publisher(a1)

# a1 = Genre(6, "alireza")
# l1.update_genre(a1)

# a1 = Designer(11, "alireza", "rezaei")
# l1.update_designer(a1)

# a1 = Source(51, "alireza", "ahmad")
# l1.update_source(a1)

# a1 = Translator(11, "alireza", "rezaei")
# l1.update_translator(a1)
