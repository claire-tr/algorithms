/*
Use an approach to "stack" the next element

hasNext: check whether there's element in the list, and the "stack", move the next element into stack
Next: return from the stack then call hasNext, or call hasNext then return.
peek: return the element in stack
=========================================================================================================
Modified version after viewing the discussion board:
- Always cache (yes, cache is the right word) the next in the next variable.
// It is much better, avoid confusing structure, and can save trouble
- When designing, not only think about to make it work. Think more about how to make it reasonable, clear, and can easily modified for future design.
 So a good design should put the "updating the next variable" part in the next(). 
 In the previous design, I had a hard time on how to deal with the last element in the list
- Don't implement the same function in different places
// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {
    private Integer next;
    private Iterator<Integer> iter;

	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    iter = iterator;
	    if(iter.hasNext())
	        next = iter.next();
	    
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return next;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    Integer res = next;
	    next = iter.hasNext()?iter.next():null;
	    return res;
	}

	@Override
	public boolean hasNext() {
	    return next!=null;
	    
	}
}

*/
