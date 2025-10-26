# Arrays and Strings Summary

## Key Similarities
- Both represent ordered collections of elements
- Fundamental structures for algorithm problems
- Share many problem-solving techniques

## Language Implementations
| Language | Array Type       | String Mutability |
|----------|------------------|-------------------|
| Python   | List (dynamic)   | Immutable         |
| Java     | ArrayList        | Immutable         |
| C++      | std::vector/array| Mutable           |

## Mutability Considerations
- **Mutable**: Can modify elements in-place (e.g. C++ strings, Python lists)
- **Immutable**: Requires creating new objects for modifications (e.g. Python/Java strings)
- Performance implications for large datasets

## Time Complexity Table
| Operation          | Time Complexity | Notes                     |
|--------------------|-----------------|---------------------------|
| Access             | O(1)            | Direct index access       |
| Append             | O(1)*           | *Amortized for dynamic arrays |
| Insert/Delete      | O(n)            | Requires shifting elements |
| Concatenation      | O(n)            | Depends on implementation |
| Substring/Slice    | O(k)            | k = length of result      |

## Key Takeaways
1. Know your language's specific implementations
2. Consider mutability when choosing operations
3. Prefer O(1) operations when possible
4. Practice common patterns for interview problems