def solution(genre, plays):
    map = {}
    cnt = {}
    for i in range(len(genre)):
        if genre[i] in cnt:
            cnt[genre[i]]+=plays[i]
        else : cnt[genre[i]] = plays[i]
        map[genre[i]+str(i)] = plays[i]
    cnt = dict(sorted(cnt.items(), key=lambda x:x[1], reverse=True))
    map = dict(sorted(map.items(), key=lambda x:x[1], reverse=True))
    res = []
    for i in cnt:
        for n in [int(k.replace(i,"")) for k, v in map.items() if k.startswith(i)][:2]:
            res.append(n)
    return res


genre = ["classic", "pop", "classic", "classic", "pop"];
plays = [500, 600, 150, 800, 2500];
print(solution(genre, plays))



from collections import defaultdict
def solution(genres, plays):
    answer = [];
    genres_plays = defaultdict(int);
    genres_songs = defaultdict(lambda: [])
    i = 0;
    for g, p in zip(genres, plays):
        genres_plays[g] += p;
        genres_songs[g].append((i, p))
        i += 1;
    sorted_genres = sorted(genres_plays.items(), key=(lambda x: x[1]), reverse = True)
    for g in sorted_genres:
        sorted_g = sorted(genres_songs[g[0]], key=(lambda x: x[1]), reverse=True)
        answer.append(sorted_g[0][0])
        if len(sorted_g) > 1:
            answer.append(sorted_g[1][0])
    return answer