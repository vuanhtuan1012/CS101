trau_profile = {
    'name': 'Trau',
    'job': 'Thuc tap sinh',
    'org': 'Trung tam khoa hoc VN',
}
william_profile = {
    'name': 'William',
    'job': 'Thuc tap sinh',
    'org': 'Trung tam khoa hoc VN',
}
tre_profile = {
    'name': 'Tre',
    'job': 'Tro ly robot',
    'org': 'Trung tam khoa hoc VN',
}
profiles = [trau_profile, william_profile, tre_profile]

def search_profile(keyword):
    for profile in profiles:
        if keyword == profile['name']:
            return profile

print('== TIM KIEM HO SO ==')
keyword = input('Nhap ten: ')
profile = search_profile(keyword)
print(profile)