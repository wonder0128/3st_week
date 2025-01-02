genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 1. 속한 노래가 많이 재생된 장르를 먼저 수록 
#   -> genre_array에서 genre별로 재생횟수를 모두 모아서 비교, 가장 많이 재생된 장르 별로 노래를 2곡씩 넣어줌.
#       ** 어떤 값이 올지 모름
#       ** 특정 키 갑셍 대해서 value를 모아서 합쳐준다.
#       ** 특정 기 값은 아직 정해지지 않았다
#           => dict = {}
#   -> 가장 많이 재생된 장르들을 순서대로

# 2. 장르 내에서 많이 재생된 노래를 먼저 수록 
#   -> 많이 재생된 장르 별로 2곡을 넣어줄 때, 많이 재생된 노래 먼저 넣어줌
#   -> 장르 별로 인덱스와 재생횟수를 저장
#       => dict = {}

# 3. 장르 내에서 재생 횟수가 같으면, 고유 번호가 낮은, 즉 인덱스가 낮은 노래 먼저 수록

# 정렬을 사용해서 문제 풀이
def get_melon_best_album(genre_array, play_array):
    # 1. dict에 장르 별로 얼마나 재생 횟수를 가지고 있는가
    # 2. dict에 장르 별로 어느 인덱스에 몇 번 재생 횟수를 가지고 있는가
    
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}

    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre in genre_total_play_dict: # classic이라는 키 값이 있다면
            genre_total_play_dict[genre] += play # 재생횟수를 더함
            genre_index_play_array_dict[genre].append([i, play])
        else: # 키 값이 없다면?
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]

    # 3. 장르 별로 가장 재생 횟수가 많은 장르들 중, 곡수가 많은 순서대로 2개씩 출력
    # 재생횟수를 기준으로 내림차순 정렬
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)

    result = []
    for genre, total_play in sorted_genre_play_array:
        print(genre, total_play)

        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key= lambda item: item[1], reverse=True)
        print('sorted_genre_index_play_array', sorted_genre_index_play_array)

        # 장르 별로 제일 잘나가는 2곡만 넣어라
        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count >= 2:
                break
            result.append(index)
            genre_song_count += 1
    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))