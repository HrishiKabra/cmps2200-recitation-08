# CMPS 2200 Recitation 08

## Answers

**Name:** Hrishi Kabra
**Name:** Petra Radmanovic


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**

  Each vertex is taken from the priority queue once - $O(V log V)$
  Each edge can cause heap push - $O(E log V)$
  Other operations are $O(V)$ or $O(E)$ hence total work = $O((V+E) log V)$
  
  Span - Dijkstra's algorithm is sequential - need to extract min vertex before processing neighbours - each extraction depends on previous one - hence span = work = $O((V+E) log V)$

