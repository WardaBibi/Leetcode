class Solution:
    def compress(self, chars: List[str]) -> int:
        count=1
        writeAt=0
        for i in range(1,len(chars)+1):
            if i<len(chars) and chars[i]==chars[i-1]:
                count+=1
            else:
                chars[writeAt]=chars[i-1]
                writeAt+=1
                if count>1:
                    for k in str(count):
                        chars[writeAt]=k
                        writeAt+=1
                    count=1
        del chars[writeAt:]
        return writeAt 

            
