import json

fileName = 'youtube.txt'


def load_data():
    try:
        with open(fileName, 'r') as file:
            test = json.load(file)
            # print('type test = ', type(test))
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(fileName, 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print('\n')
    print('*' * 70)
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video['name']}, Duration: {video['time']}')
    print('*' * 70)


def add_video(videos):
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video no to UPDATE: '))
    if 1 <= index <= len(videos):
        name = input('Enter the new video name: ')
        time = input('Enter the new video time: ')
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print('Video Updated Successfully!')
    else:
        print('Invalid index selected!')


def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video no to DELETE: '))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print('Video Deleted Successfully!')
    else:
        print('Invalid index selected! ')


def main():
    videos = load_data()
    while True:
        print('\n Youtube Manager | choose an option')
        print('1. LIST all Youtube videos')
        print('2. ADD a Youtube video')
        print('3. UPDATE a Youtube video detail')
        print('4. DELETE a Youtube video')
        print('5. EXIT the App')
        choice = input('Enter Your Choice: ')
        # print('videos = ', videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Invalid Choice')


if __name__ == "__main__":
    main()
