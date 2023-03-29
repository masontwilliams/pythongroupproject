from student import Student

#
# Billing class
#

from student import Student


class Billing(Student):
    def __init__(self, id, c_roster, c_max_size, s_in_state, c_rosters, c_hours):
        super().__init__(id, c_roster, c_max_size)
        self.id = id
        self.s_in_state = s_in_state
        self.c_rosters = c_rosters
        self.c_hours = c_hours
        self.hours = 4
        self.bill = 0

    def calculate_hours_and_bill(self):
        keylst = []
        for i in self.c_rosters:  # for loop to calculate the hours
            if self.id in self.c_rosters[i]:
                keylst.append(i)
        h = 0
        for x in keylst:
            h += self.c_hours.get(x)
        self.hours = h
        if self.id in self.s_in_state:  # checking to see if id is in dictionary of in state students
            self.bill = 225 * self.hours
        else:
            self.bill = 850 * self.hours

        return self.hours, self.bill * h

    def display_hours_and_bill(self):
        self.calculate_hours_and_bill()
        return f'Course load: {self.hours} credit hours \nEnrollment cost: {self.bill}'

    def __str__(self):
        return f'Course load: {self.hours} credit hours \nEnrollment cost: {self.bill}'
