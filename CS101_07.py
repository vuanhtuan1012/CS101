#### BT1
def push(stack, value):
    stack.append(value)
    return stack

# commands to test
stack = [2, 6, 9]
push(stack, 1)


#### BT2
def pop(stack):
    if stack:
        stack.pop()
    return stack

# commands to test
stack = [2, 6, 9, 1, 4, 3]
pop(stack)


#### BT3
def enqueue(queue, value):
    queue.append(value)
    return queue

# commands to test
queue = [2, 6, 9, 1]
enqueue(queue,  4)


#### BT4
def dequeue(queue):
    if queue:
        queue.pop(0)
    return queue

# commands to test
queue = [2, 6, 9, 1, 4]
dequeue(queue)


#### BT5
def get_average_score(profiles):
    tong_diem = 0
    for student in profiles:
        tong_diem += student["score"]
    diem_trung_binh = tong_diem / len(profiles)
    return diem_trung_binh

# commands to test
profiles = [{'name': 'Trau', 'score': 8}]
get_average_score(profiles)
profiles = [{'name': 'Trau', 'score': 8},
            {'name': 'Tre', 'score': 9},
            {'name': 'Tran', 'score': 9},
            {'name': 'Tri', 'score': 8}]
get_average_score(profiles)


#### BTCB
def update_stack(stack, actions):
    # dinh nghia ham push
    def push(stack, value):
        stack.append(value)
        return stack

    # dinh nghia ham pop
    def pop(stack):
        if len(stack) > 0:
            stack.pop()
        return stack

    # di qua cac phan tu trong mang action
    index = 0
    while index < len(actions["action"]):
        hanh_dong = actions["action"][index]
        sach = actions["book"][index]
        if hanh_dong == "push":
            push(stack, sach)
        if hanh_dong == "pop":
            pop(stack)
        index += 1
    return stack

# commands to test
stack = []
actions = {'action': ['push', 'push'],  'book': ['Doraemon', 'Conan']}
update_stack(stack, actions)

stack = ['Doraemon', 'Conan', 'Lao Hac']
actions = {'action': ['push', 'pop', 'push'],  'book': ['Truyen Kieu', None, 'Doraemon']}
update_stack(stack, actions)

stack = ['Doraemon']
actions = {'action': ['push', 'pop', 'pop'],  'book': ['Conan', None, None]}
update_stack(stack, actions)


#### BTNC
def check_valid_parentheses(text):
    valid_opening = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ki_tu in text:
        if ki_tu == "(" or ki_tu == "[" or ki_tu == "{":
            stack.append(ki_tu)
        if ki_tu == ")" or ki_tu == "]" or ki_tu == "}":
            if not stack:
                return False
            item = stack.pop()
            if item != valid_opening[ki_tu]:
                return False
    if stack:
        return False
    return True

# commands to test
check_valid_parentheses('()')
check_valid_parentheses('()[]{}')
check_valid_parentheses('(]')