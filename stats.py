def get_num_words(bookstring):
    count = 0
    countarray = bookstring.split()
    count = len(countarray)

    return count

def get_char_counts(bookstring):
        bookstring = bookstring.lower()
        results = {}
        for i in range(0,len(bookstring)):
            if (bookstring[i] in results):
                results[bookstring[i]] +=  1
            else:
                results[bookstring[i]] = 1
        return results

def sort_on(dict):
    return dict["num"]


def sorted_list(dict):
    sorted = []
    for k,v in dict.items():
        d = {"char" : k, "num": v}
        sorted.append(d)
    sorted.sort(reverse=True,key=sort_on)

    return sorted


            