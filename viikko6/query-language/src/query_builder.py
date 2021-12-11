from matchers import All, HasAtLeast, HasFewerThan, PlaysIn, And, Or

class QueryBuilder:
    def __init__(self, query_builder = All()):
        self.query_builder = query_builder

    def build(self):
        return self.query_builder

    def playsIn(self, player):
        return QueryBuilder(And(self.query_builder, (PlaysIn(player))))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_builder, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_builder, HasFewerThan(value, attr)))

    def oneOf(self, matcher, matcher2):
        return QueryBuilder(Or(matcher, matcher2))