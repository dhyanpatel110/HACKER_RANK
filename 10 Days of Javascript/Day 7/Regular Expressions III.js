/* THERE ARE TWO METHOD TO SOLVE THIS EXAMPLE */

/* METHOD(1) */
function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match ALL occurrences of numbers in a string.
     */
    
      let re = /\d+/g;
    /*
     * Do not remove the return statement
     */
    return re;
}

/* METHOD(2)*/
function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match ALL occurrences of numbers in a string.
     */
    
    var re = RegExp('\\d+', 'g');
    
    /*
     * Do not remove the return statement
     */
    return re;
}
