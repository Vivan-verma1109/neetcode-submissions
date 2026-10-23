class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.heaps = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = (cuisine, rating)
            heapq.heappush(self.heaps.setdefault(cuisine,[]),(-rating,food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foods[food]
        self.foods[food] = (cuisine,newRating)
        heapq.heappush(self.heaps[cuisine],(-newRating,food))
    
    def highestRated(self, cuisine: str) -> str:
        heap=self.heaps[cuisine]
        while -heap[0][0] != self.foods[heap[0][1]][1]:
            heapq.heappop(heap)
        return heap[0][1]
