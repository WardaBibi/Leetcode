function StringChallenge(str)
{
  var stack=[];
  let startTag;
  let endTag;
  var domListNew=str.match(/<\w+>|<\/\w+>/g)

  for (var i = 0; i < domListNew.length; i++) {
    if ( domListNew[i][1] !== '/' ) {
      stack.push(domListNew[i])
    }
    else
    {
      
      startTag=stack.pop().replace(/<|>/g,'')
      endTag=domListNew[i].replace(/\/|<|>/g,'')
      if (startTag == endTag)
        {
          continue
        }
      else
        {
          return startTag
        }
      
    }
   
  }
  // console.log(strcm)
  return "true"
  
}

console.log(StringChallenge("<div><div><b>hello</b></div></p>")); // div
console.log(StringChallenge("<div>abc</div><p><em><i>test test test</b></em></p>")); // i
console.log(StringChallenge("<div><i>hello</i>world</b>"));
console.log(StringChallenge("<div><b><p>hello world</p></b></div>")); // Expected Output: true
console.log(StringChallenge("<div><div><b></b></div></p>")); // Expected Output: div
console.log(StringChallenge("<div>abc</div><p><em><i>test test test</b></em></p>")); // Expected Output: i
console.log(StringChallenge("<div><p>hello</div></p>")); // Expected Output: div
console.log(StringChallenge("<div><i>hello</i>world</div>")); // Expected Output: true
console.log(StringChallenge("<div><b>hello</div></b>")); // Expected Output: div
console.log(StringChallenge("<div><p><i></i></p></div>")); // Expected Output: true
console.log(StringChallenge("<div><i>hello</b></i>")); // Expected Output: i
console.log(StringChallenge("<div><b>hello</i></b>")); // Expected Output: b
console.log(StringChallenge("<div><p>hello</div></p>")); // Expected Output: div
console.log(StringChallenge("<div>hello</p></div>")); // Expected Output: div
console.log(StringChallenge("<div><p><b></b></p></div>")); // Expected Output: true




