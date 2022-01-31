import re, csv


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def correct_number(contacts_list):
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_update = list()
    for data in contacts_list:
        data_string = ','.join(data)
        formatted_data = re.sub(number_pattern_raw, number_pattern_new, data_string)
        data_list = formatted_data.split(',')
        contacts_list_update.append(data_list)
    return contacts_list_update


def name_format(contacts_list):
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    contacts_list_update = list()
    for data in contacts_list:
        data_string = ','.join(data)
        formatted_data = re.sub(name_pattern_raw, name_pattern_new, data_string)
        data_list = formatted_data.split(',')
        contacts_list_update.append(data_list)
    return contacts_list_update


def duplis(contacts_list):
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i != j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
    contacts_list_update = list()
    for data in contacts_list:
        if data not in contacts_list_update:
            contacts_list_update.append(data)
    return contacts_list_update


def write_correct_file(contacts_list):
    with open("contactbook.csv", "w") as user_file:
        data_writer = csv.writer(user_file, delimiter=',')
        data_writer.writerows(contacts_list)


if __name__ == '__main__':
    contacts = read_file('phonebook_raw.csv')
    contacts = correct_number(contacts)
    contacts = name_format(contacts)
    contacts = duplis(contacts)
    write_correct_file(contacts)