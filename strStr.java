class Solution {
    public int strStr(String haystack, String needle) {
        int lengthOfHaystack = haystack.length();
        int lengthOfNeedle = needle.length();
        int answer = -1;
        if(lengthOfNeedle == 0){
            return 0;
        }
        if(lengthOfNeedle == lengthOfHaystack){
            if(haystack.equals(needle)){
                return 0;
            }
            else{
                return -1;
            }
        }
        for(int i = 0; i <= lengthOfHaystack - lengthOfNeedle; i++)
        {
            int j;
            for( j = 0; j < lengthOfNeedle; j++)
            {
                if(haystack.charAt(i+j) != needle.charAt(j))
                    break;
            }
            
            if(j == lengthOfNeedle)
            {
                return i;
            }
        }
        return -1;
}
}
