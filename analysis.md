# Analysis Questions and Answers
 ## Q1: Why does the linked stack push at the head instead of the tail?
 Pushing and popping at the head takes only O(1) constant time. If we operated at the tail, we would need to traverse the entire list every time to find the second-to-last node, which would slow operations down to O(n). The head is always immediately accessible, making operations fast and efficient.
 ## Q2: Why must the array queue be circular?
 In a simple linear queue, every dequeue moves the front index forward, leaving unused empty space at the beginning of the array that cannot be filled again. Eventually, the queue reports "full" even though there is actually free space — this is called false overflow. By using the modulo % operator, a circular queue lets the indices wrap around and reuse those empty positions. This uses memory efficiently and keeps both enqueue and dequeue operations at O(1) time complexity.
