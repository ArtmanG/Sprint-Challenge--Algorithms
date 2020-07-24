#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is O(n) because it runs for as long as a < n, and increases by a factor of n * n.

b) This is O(n log n) because the inner loop increments at a greater rate.

c) This is O(n) because it recursively returns an amount that's roughly equal to n.

## Exercise II

<!-- If a build is n stories tall, you could walk up each flight of stares starting at the bottom, and drop an egg until you find the floor where eggs go splat. Linear style. -->

Binary will be faster, especially if these are super unbreakable eggs and you have a skyscraper.
if a building is n stories tall.
you start to the middle floor (n // 2) and if the egg breaks you knw all the floors above it will break eggs too. 
you set the middle again with the new high (low + (mid -1 = new high)) // 2 = new mid1, if there it doesn't break you know all floors below are safe so,
You go up to to a new mid again and set the new low, ((new mid1 + 1 = new low) + high) // 2 = new mid2 and so on, until you find the f floor.

arr = [1, ..., n]

safe_eggs(arr):
    highest (floor we should go to) = top floor
    lowest (floor we should go to) = ground floor

    while low <= high:
        middle floor = (high + low) // 2

now with this we don't actually know the target as with a classic binary search, (or the target is a condition we are trying to meet) so even if mid == safe eggs, it does not mean mid == the most safe eggs. we maybe could still go up one, or two floors and have safe eggs. So we can't assume the first safe egg is ok to stick with.

        if target < arr[mid]:
                highest = middle floor - 1 (the floor below)
        if target > arr[mid]:
                lowest = middle floor + 1 (the floor above)        
        once target(floor + 1 = broken, floor -1 = safe, target floor = safe) == arr[mid]:
                return mid

once we find the highest floor we can safely drop eggs from then we know that. and the time complexity of a binary search is O(log2n). But I guarantee that linear is faster than this because if you start from the bottom, you stop immediately as the egg breaks on the first floor and you only loose one egg.




<!-- if a building is n stories tall and an egg only breaks if it is thrown off of f or higher then,
as long as you are only dropping eggs at f or lower the eggs should be safe (for real what is f? 
.0001% of the first floor)
safe_eggs:
    for n in building:
        if n is less than f:
            return safe eggs
        else:
            return haha eggs go splat

A for loop is used here so the time complexity is O(log n) -->
