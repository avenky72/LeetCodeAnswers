/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let longest = 0;
    const subs = [];
    for (let i = 0; i < s.length; i++){
        while (subs.includes(s[i])){
            subs.shift();
        }
        subs.push(s[i]);
        longest = Math.max(longest, subs.length);
        }
    return longest;
    }
