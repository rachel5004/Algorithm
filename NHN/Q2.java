package NHN;
import java.util.*;
import java.util.Map.Entry;

class Main {
   private static void solution(int region, int attack, int[][] arr) {
        Map<Integer,Integer> countMap = new HashMap<Integer,Integer>();
       for (int i = 0; i < arr.length; i++) {
            int[] inArr = arr[i];
            for (int j = 0; j < inArr.length; j++) {
                countMap.merge(inArr[j], 1, Integer::sum);
            }
        }
		List<Entry<Integer, Integer>> list_entries = new ArrayList<Entry<Integer, Integer>>(countMap.entrySet());

		// 비교함수 Comparator를 사용하여 내림 차순으로 정렬
		Collections.sort(list_entries, new Comparator<Entry<Integer, Integer>>() {
			public int compare(Entry<Integer, Integer> obj1, Entry<Integer, Integer> obj2){
				// 내림 차순으로 정렬
				return obj2.getValue().compareTo(obj1.getValue());
			}
		});
        int answer =0;
        for (int i=0;i<attack;i++) {
            answer=answer+list_entries.get(i).getValue();
        }
        System.out.println(answer);
   }
   private static class InputData {
       int region;
       int attack;
       int[][] frequencies;
   }
   private static InputData processStdin() {
       InputData inputData = new InputData();
       try (Scanner sc = new Scanner(System.in)) {
           String[] tmp = sc.nextLine().split(" ");
           inputData.region = Integer.parseInt(tmp[0]);
           inputData.attack = Integer.parseInt(tmp[1]);
           inputData.frequencies = new int[inputData.region][];

           for(int i=0;i<inputData.region;i++) {
               tmp = sc.nextLine().split(" ");
               int numOfFrequencies = Integer.valueOf(tmp[0]);
               inputData.frequencies[i] = new int[numOfFrequencies];
               for(int j=0;j<numOfFrequencies;j++) {
                   inputData.frequencies[i][j] = Integer.parseInt(tmp[j+1]);
               }
           }
       }catch (Exception e) { throw e; }
       return inputData;
    }
    public static void main(String[] args) throws Exception{
        InputData inputData = processStdin();
       solution(inputData.region,inputData.attack,inputData.frequencies);
   }
}