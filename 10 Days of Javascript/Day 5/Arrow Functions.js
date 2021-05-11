/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
    const func = nums.map(function(num){
        
        /* CHECK ELEMENT IS EVEN OR ODD */
        /* EVEN MULTIPLY THE ELEMENT BY 2 */
        if(num%2 == 0){
            return 2*num;
        }
        
        /* ODD MULTIPLY THE ELEMENT BY 3 */
        else{
            return 3*num;
        }
    });
    return func;
}
