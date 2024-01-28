package Programmers;

import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.stream.Collectors;

/*
https://school.programmers.co.kr/learn/courses/30/lessons/81301
숫자 문자열과 영단어
 */
public class Failure {

    private static int[] getResult(int N, int[] stages) {
        stages = Arrays.stream(stages).sorted().toArray();
        Map<Integer, Integer> lv = new LinkedHashMap<>();
        int total = stages.length;
        for (int i = 0; i < N; i++) {
            int member = Collections.frequency(List.of(stages), stages[i]);
            if (member == 0) {
                lv.put(i+1, 0);
            } else {
                lv.put(i+1, member / total);
            }
            total -= member;
        }
        List<Map.Entry<Integer, Integer>> entryList = new LinkedList<>(lv.entrySet());
        entryList.sort(Map.Entry.comparingByValue());
        return entryList.stream()
            .map(Entry::getKey)
            .mapToInt(i -> i)
            .toArray();

    }


    public static void main(String[] args) {
        int n = 5;
        int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};

        System.out.println(Arrays.toString(getResult(n, stages)));
    }
}
