package NHN;

import java.util.*;
import java.util.stream.IntStream;


public class Q3 {
   private static void solution(int numconflicts,int[][] conflicts) {
        int total = factorial(8);
        int tmp = factorial(7)*conflicts.length;
        int con =  factorial(7)*factorial(conflicts.length)*conflicts.length;
        System.out.println(total-tmp);
        // int[] res = {};
        // for (int[] arr: conflicts) {
        //     res = IntStream.concat(IntStream.of(res), IntStream.of(arr)).toArray();
        // }
        // Set<Integer> set = new HashSet<Integer>();
		// for(int i : res) set.add(i);
		
		// List<Integer> list = new ArrayList<Integer>(set);

        // for(int i : list)
		// 	System.out.print(i + " ");
   }
   private static int factorial(int n) {
       if(n==1) return 1;
       return n* factorial(n-1);
   }
   private static class InputData {
       int numconflicts;
       int[][] conflicts;
   }
   private static InputData processStdin() {
       InputData inputData = new InputData();
       try (Scanner sc = new Scanner(System.in)) {
           inputData.numconflicts = Integer.parseInt(sc.nextLine());
           inputData.conflicts = new int[inputData.numconflicts][2];
           for(int i=0;i<inputData.numconflicts;i++) {
                String[] tmp = sc.nextLine().split(" ");
               inputData.conflicts[i][0] = Integer.parseInt(tmp[0]);
               inputData.conflicts[i][1] = Integer.parseInt(tmp[1]);
           }
       }catch (Exception e) { throw e; }
       return inputData;
    }
    public static void main(String[] args) throws Exception{
        InputData inputData = processStdin();
       solution(inputData.numconflicts,inputData.conflicts);
   }
}