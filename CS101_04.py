#### BT1
def sing_happy_birthday(name):
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday Dear " + name)
    print("Happy Birthday to You")

# command to test in shell
sing_happy_birthday("Thuy")


#### BT2
def paper_price(length, width):
    so_tien = length * width * 2
    return so_tien

# commands to test in shell
paper_price(10, 5)
paper_price(25, 12)


#### BT3
def largest(a, b):
    if a > b:
        return a
    return b

# commands to test in shell
largest(5, 9)
largest(113, 25)


#### BT4
def check_condition(gender, height, weight):
    if gender == "nam":
        if height >= 165 and weight >= 54:
            return True
    if gender == "nu":
        if height >= 160 and weight >= 48:
            return True
    return False

# commands to test in shell
check_condition('nam', 175, 52)
check_condition('nu', 176, 50)


#### BT5
def calculate_score(trials):
    tong = 0
    for diem_thu_nghiem in trials:
        tong += diem_thu_nghiem
    tbc = tong / len(trials)
    return tbc

# commands to test in shell
calculate_score([80, 84, 85])
calculate_score([77, 84, 90])


#### BTCB
def who_is_winner(votes):
    thi_sinh_1 = votes[0]
    thi_sinh_2 = ""
    vote_1 = 0
    vote_2 = 0
    for thi_sinh in votes:
        if thi_sinh == thi_sinh_1:
            vote_1 += 1
        else:
            if vote_2 == 0:
                thi_sinh_2 = thi_sinh
            vote_2 += 1
    if vote_1 > vote_2:
        return thi_sinh_1
    elif vote_1 == vote_2:
        return "Both"
    else:
        return thi_sinh_2

# commands to test in shell
who_is_winner(["Trau", "Trau", "William", "Trau"])
who_is_winner(["Trau", "Trau", "William", "William"])
who_is_winner(["Trau", "William", "Trau", "William", "William"])


#### BTNC
def favorite_song(songs, votes):
    counters = []
    # khoi tao mang counters
    for bai_hat in songs:
        counters.append(0)

    # dem so binh chon cua tung bai hat
    # luu vao mang counters
    for bai_hat in votes:
        index = 0
        # tim index cua bai hat trong mang songs
        while index < len(songs):
            if songs[index] == bai_hat:
                counters[index] += 1
                break
            index += 1

    # tim index cua so lon nhat trong mang counters
    index = 0
    sln = counters[0]
    index_sln = 0
    while index < len(counters):
        if sln < counters[index]:
            sln = counters[index]
            index_sln = index
        index += 1
    return songs[index_sln]

# commands to test in shell
favorite_song(["Jingle Bell", "La La La"],
              ["Jingle Bell", "La La La", "Jingle Bell",
               "Jingle Bell", "La La La", "La La La",
               "La La La", "La La La", "Jingle Bell"])
favorite_song(["Twinkle Twinkle", "Happy", "ABC"],
              ["Happy", "ABC", "Twinkle Twinkle", "Happy", "Twinkle Twinkle"])
