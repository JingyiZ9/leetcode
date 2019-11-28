## 优先队列
java中用堆实现      
https://www.cnblogs.com/luoxn28/p/5616101.html   

### 最小堆
根节点最小      

1. 插入操作
首先将元素放入堆底层末尾，然后进行上浮操作：与根节点比较        
priorityQueue.offer()       

2. 移除操作     
队列非空情况下，首先移除根节点的最小元素。将集合中末尾元素放到根节点，然后进行下沉操作：与子节点比较        
priorityQueue.poll()        

* Leetcode 378
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/      
半排序矩阵找出第k大元素
