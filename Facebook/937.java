// 找出K个离原点最近的点
//Solution 1: override sort function - 对所有点进行排序，浪费一部分点
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        Arrays.sort(points, (p1, p2) -> p1[0]*p1[0] + p1[1]*p1[1] - (p2[0]*p2[0] + p2[1]*p2[1]));
        return Arrays.copyOfRange(points, 0, K);
    }
}


//Solution 2: 最大堆 priorityQueue - 取最小K个点
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        // edge cases
        if (points==null || points.length == 0 || K < 1) return points;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> getDistanceSquare(b) - getDistanceSquare(a));
        
        for (int[] point:points) {
            pq.add(point);
            
            if (pq.size() > K) {
                pq.poll();
            }
        }
        
        int[][] res = new int[K][2];
        
        for (int i=0; i<K; i++) {
            res[i] = pq.poll();
        }
        return res;
    }
    
    public int getDistanceSquare(int[] point) {
        return point[0]*point[0] + point[1]*point[1];
    }
}