def read_chat_log(file):
    with open(file , 'r') as f:
        return f.readlines()

def parse_chat(lines):
    user_msgs = []
    ai_msgs = []
    for line in lines:
        if line.startswith('User:'):
            user_msgs.append(line[len('User:'):].strip())
        elif line.startswith('AI:'):
            ai_msgs.append(line[len('AI:'):].strip())
    return user_msgs, ai_msgs

def process_chat_file(use_tfidf=True):
    lines = read_chat_log('text.txt')
    user_msgs, ai_msgs = parse_chat(lines)
    print(user_msgs , ai_msgs)


def main():
    process_chat_file()

if __name__ == "__main__":
    main()