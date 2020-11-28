/**
 * 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
 * 并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
 */

function FirstNotRepeatingChar(str)
{
    // write code here
    var cnt = [];
    var tmp = 'A'.charCodeAt();
    for(var i = 0, len = str.length; i < len; i++){
        if(cnt[str[i].charCodeAt() - tmp] === undefined){
            cnt[str[i].charCodeAt() - tmp] = 1;
        }else{
            cnt[str[i].charCodeAt() - tmp]++;
        }
    }
    for(var i = 0, len = str.length; i < len; i++){
        if(cnt[str[i].charCodeAt() - tmp] === 1){
            return i;
        }
    }
    return -1;
}