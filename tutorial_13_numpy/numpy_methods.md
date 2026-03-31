# Common NumPy Methods Reference  
  
## Quick Reference Table  
  
| Method | Description | Input Example | Output |  
|--------|-------------|---------------|--------|  
| `np.add(a, b)` | Element-wise addition of two arrays | `np.add([10, 20, 30], [5, 15, 25])` | `[15, 35, 55]` |  
| `np.subtract(a, b)` | Element-wise subtraction of two arrays | `np.subtract([100, 200, 300], [25, 50, 75])` | `[75, 150, 225]` |  
| `np.multiply(a, b)` | Element-wise multiplication of two arrays | `np.multiply([10, 20, 30], [2, 3, 4])` | `[20, 60, 120]` |  
| `np.divide(a, b)` | Element-wise division of two arrays | `np.divide([100, 200, 300], [10, 20, 30])` | `[10.0, 10.0, 10.0]` |  
| `np.std(array)` | Calculates the standard deviation | `np.std([10, 20, 30, 40, 50])` | `14.142135623730951` |  
| `np.var(array)` | Calculates the variance | `np.var([10, 20, 30, 40, 50])` | `200.0` |  
| `np.median(array)` | Computes the median | `np.median([10, 20, 30, 40, 50])` | `30.0` |  
| `np.percentile(array, q)` | Computes the q-th percentile | `np.percentile([10, 20, 30, 40, 50], 75)` | `40.0` |  
| `np.sort(array)` | Returns a sorted copy of the array | `np.sort([50, 20, 40, 10, 30])` | `[10, 20, 30, 40, 50]` |  
| `np.argsort(array)` | Returns the indices that would sort the array | `np.argsort([50, 20, 40, 10, 30])` | `[3, 1, 4, 2, 0]` |  
| `np.unique(array)` | Finds the unique elements | `np.unique([10, 20, 10, 30, 20, 40])` | `[10, 20, 30, 40]` |  
| `np.sum(array, axis)` | Computes the sum along a specified axis | `np.sum([10, 20, 30, 40])` | `100` |  
| `np.cumsum(array)` | Returns the cumulative sum | `np.cumsum([10, 20, 30, 40])` | `[10, 30, 60, 100]` |  
| `np.clip(array, a_min, a_max)` | Limits values within a specified range | `np.clip([5, 15, 25, 35], 10, 30)` | `[10, 15, 25, 30]` |  
  
