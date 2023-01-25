from django_neomodel import DjangoNode
from neomodel import UniqueIdProperty, StringProperty, DateProperty, RelationshipTo


class Person(DjangoNode):
    spouse = RelationshipTo('.models.Person', 'MARRIED')
    children = RelationshipTo('.models.Person', 'PARENT')
    parents = RelationshipTo('.models.Person', 'CHILD')
    
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    surname = StringProperty()
    birth = DateProperty(format='%d-%m-%Y')
    death = DateProperty(format='%d-%m-%Y')
    
    class Meta:
        app_label = 'tree'
