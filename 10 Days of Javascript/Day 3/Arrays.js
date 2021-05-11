/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    
    /* SORTING ARE INPUT NUMBERS */
    var sArray = nums.sort(function(a,b){
        return a-b;
    });
    
    /* INDEXING NUMBER */
    var uSarray = sArray.filter(function(elm,index,self){
        return index == self.indexOf(elm);
    });
    
    /* RETURN SECOND LAST LARGEST NUMBER */
    return uSarray[uSarray.length-2];
}
