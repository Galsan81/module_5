import time


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)


class Video:
    def __init__(self, title: str, duration: int, time_now = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


    def __str__(self):
        return f"{self.title}"


class UrTube:
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, name: str, password: str) -> None:
        for user in self.users:
            if name == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int) -> None:
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for movie in videos:
            if not any(v.title == movie.title for v in self.videos):
                self.videos.append(movie)

    def get_videos(self, slovo: str) -> list:
        sp_video = []
        for video in self.videos:
            if slovo.lower() in video.title.lower():
                sp_video.append(video.title)
        return sp_video

    def watch_video(self, movie: str) -> None:
        if self.current_user and self.current_user.age < 18: # возрастное условие
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(video.time_now+1, video.duration+1):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __str__(self):
        return f"{self.videos}"


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
