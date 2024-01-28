package Programmers;

import java.util.Arrays;

public class ArcheryCompetition {

    static int[] res = {-1};
    static int[] lion = new int[11];
    static int max = -1000;

    public static void dfs(int[] info, int n, int cnt) {
        if (cnt == n + 1) {
            int apeach_point = 0;
            int lion_point = 0;
            for (int i = 0; i <= 10; i++) {
                if (info[i] != 0 || lion[i] != 0) {
                    if (info[i] < lion[i]) {
                        lion_point += 10 - i;
                    } else {
                        apeach_point += 10 - i;
                    }
                }
            }
            if (lion_point > apeach_point) {
                if (lion_point - apeach_point >= max) {
                    res = lion.clone();
                    max = lion_point - apeach_point;
                }
            }
            return;
        }
        for (int j = 0; j <= 10 && lion[j] <= info[j]; j++) {
            lion[j]++;
            dfs(info, n, cnt + 1);
            lion[j]--;
        }
    }


    public static void main(String[] args) {
        int n = 5;
        int[] info = {2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0};
        dfs(info, n, 1);
        System.out.println(Arrays.toString(res));
    }


}
