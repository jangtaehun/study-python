class Book:
    def set_info(self, name, written):
        self.name = name
        self.written = written
        print(f'제목: {self.name}, 저자: {self.written}')

book1 = Book()
book1.set_info("python", 'jangth')


class Song:
    def set_song(self, song, category):
        self.song = song
        self.category = category

    def print_song(self):
        print(f'노래 제목: {self.song}({self.category})')

class Singer:
    def set_singer(self, name):
        self.name = name

    def hit_song(self, song):
        print(f'가수 이름: {self.name}')
        print(f'노래 제목: {song.song}')

# Song 인스턴스 생성
song = Song() #값이 없는 인스턴스 생성 -> 값을 저장할 수 있는 메소드 호출
song.set_song('취중진담', '발라드')

# Singer 인스턴스 생성
singer = Singer()
singer.set_singer('김동률')

# Singer의 대표곡 지정
singer.hit_song(song)

# Song 정보 출력
# song.print_song()
