class Guest:
    def __init__(self, row):
        self.count_adults = row.adults
        self.count_children = row.children
        self.count_babies = row.babies
        self.country = row.country
        self.customer_type = row.customer_type

    def __str__(self):
        return 'This guest includes ' + self.count_adults + \
            'adults, and ' + self.count_children + 'children, and ' \
            + self.count_babies + 'babies. /n from the country of ' + self.country