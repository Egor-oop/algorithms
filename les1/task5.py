class PlateStackClass:
    def __init__(self, max_size):
        self.elems = []
        self.max_size = max_size

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return str(self.elems)

    def push_in(self, el):
        if len(self.elems[len(self.elems)-1]) < self.max_size:
            self.elems[len(self.elems)-1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems)-1].append(el)

    def pop_out(self):
        result = self.elems[len(self.elems)-1].pop()
        if len(self.elems[len(self.elems)-1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):
        return self.elems[len(self.elems)-1][len(self.elems[len(self.elems)-1])-1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elems)


if __name__ == '__main__':
    plates = PlateStackClass(3)
    plates.push_in('Plate1')
    plates.push_in('Plate2')
    plates.push_in('Plate3')
    plates.push_in('Plate4')
    plates.push_in('Plate5')
    print(plates)
    print(plates.pop_out())
    print(plates.get_val())
    print(plates.stack_size())
    print(plates.stack_count())
    print(plates)
