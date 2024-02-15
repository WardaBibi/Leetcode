function palindrome(str){
  const initialStr = str;
  const reversedStr = str.split('').reverse().join('');
  return initialStr === reversedStr;
}

console.log(palindrome("eye")); // Output: true
console.log(palindrome("racecar")); // Output: true
console.log(palindrome("hello")); // Output: false
console.log(palindrome("A man, a plan, a canal, Panama")); // Output: true
console.log(palindrome("121")); // Output: false
