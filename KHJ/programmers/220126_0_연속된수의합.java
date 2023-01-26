import java.util.stream.*;

class Solution {
    public int[] solution(int num, int total) {
        int base = (total - IntStream.range(0,num).sum())/num;
        int[] answer = IntStream.range(0,num).map(i -> base + i).toArray();
        
        return answer;
    }
}