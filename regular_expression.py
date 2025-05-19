










def read_chat_log(file):
    with open(file , 'r') as f:
        return f.readlines()



def process_chat_file(use_tfidf=True):
    lines = read_chat_log('text.txt')
    print(lines)


def main():
    process_chat_file()

if __name__ == "__main__":
    main()