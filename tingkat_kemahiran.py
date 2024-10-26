def check_data_input(data_line, doc):
    nilai = []
    check_data = True
    split_data_line = data_line.split(",")
    if len(split_data_line) != N:
        check_data = False
        print("Jumlah input %s tidak sesuai dengan banyaknya lawan" % doc)
    else:
        for data_kemahiran in split_data_line:
            if int(data_kemahiran) < 1 or int(data_kemahiran) > 1000:
                check_data = False
                print("Nilai %s tidak boleh lebih kecil dari 1 atau tidak boleh lebih dari 1000" % doc)
                break
            else:
                nilai.append(int(data_kemahiran))

    return {'check_data':check_data, 'nilai': nilai}

def max_skill_level(N, M, Ai, Bi):
    players = sorted(zip(Ai, Bi)) 
    current_skill = M

    for skill, bonus in players:
        if skill <= current_skill:
            current_skill += bonus
        else:
            break

    return current_skill

first_line = input("Input jumlah lawan dan tingkat kemahiran awal (e.g. 4, 5): ")
N = 0
M = 0
if "," in first_line:
    split_first_line = first_line.split(",")
    if len(split_first_line) > 2:
        print("Jumlah inputan tidak sesuai dengan yang di contohkan")
    elif int(split_first_line[0]) < 1:
        print("Jumlah lawan tidak boleh kurang dari 1")
    elif int(split_first_line[1]) > 100:
        print("Nilai tingkat kemahiran tidak boleh lebih besar dari 100")
    else:
        N = int(split_first_line[0])
        M = int(split_first_line[1])
else:
    print("Format input jumlah lawan dan tingkat kemahiran belum sesuai")

Ai = False
check_data_second_line = True
if N > 0 and M > 0:
    second_line = input("Input tingkat kemahiran lawan sesuai dengan banyaknya lawan (e.g. 4, 2, 6, 7): ")
    if "," in second_line:
        result_check_data = check_data_input(second_line, 'tingkat kemahiran lawan')
        if result_check_data['check_data']:
            Ai = result_check_data['nilai']
        else:
            check_data_second_line = result_check_data['check_data']
    else:
        print("Format input tingkat kemahiran lawan belum sesuai")

Bi = False
check_data_third_line = True
if check_data_second_line:
    third_line = input("Input bonus kemahiran sesuai dengan banyaknya lawan (e.g. 4, 2, 6, 7): ")
    if "," in third_line:
        result_check_data = check_data_input(third_line, 'bonus kemahiran')
        if result_check_data['check_data']:
            Bi = result_check_data['nilai']
        else:
            check_data_third_line = result_check_data['check_data']
    else:
        print("Format input bonus kemahiran belum sesuai")

if N > 0 and M > 0 and check_data_second_line and check_data_third_line:
    print(max_skill_level(N, M, Ai, Bi))
