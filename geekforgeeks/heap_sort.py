class Solution:
    def heapify(self, heap, n, current_idx):
        largest = current_idx
        left = 2 * current_idx + 1
        right = 2 * current_idx + 2
        
        if left < n and heap[left] > heap[largest]:
            largest = left
        
        if right < n and heap[right] > heap[largest]:
            largest = right
        
        if largest != current_idx:
            heap[current_idx], heap[largest] = heap[largest], heap[current_idx]
            self.heapify(heap, n, largest)
    
    def buildHeap(self, arr, n):
        
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
       
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0] 
            self.heapify(arr, i, 0) 
        