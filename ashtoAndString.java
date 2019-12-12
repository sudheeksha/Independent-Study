import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Suffix{
    int rank,nextRank;
    int value;
}

class Comp implements Comparator<Suffix>{
    @Override
    public int compare(Suffix suffix_1,Suffix suffix_2){
        if(suffix_1.rank == suffix_2.rank)  
            return suffix_1.nextRank - suffix_2.nextRank;
        else    
            return suffix_1.rank - suffix_2.rank;
    }
}
public class Solution {

    public static int[] getSuffixArray(String str){
        int n = str.length();
        Suffix temp[] = new Suffix[n];
        for(int i=0;i<n;i++){
            temp[i] = new Suffix();
            temp[i].value = i;
            temp[i].rank = str.charAt(i)-'a';
            if(i == n-1)
                temp[i].nextRank = -1;
            else
                temp[i].nextRank = str.charAt(i+1)-'a';
        }
        Comp cc = new Comp();
        Arrays.sort(temp,cc);
        for(int k=4; k<2*n; k=k*2){
            int tr[] = new int[n];
            int rank = 0;

            for(int i=1;i<n;i++){
                if(temp[i].rank==temp[i-1].rank &&temp[i].nextRank==temp[i-1].nextRank)
                    tr[i] = rank;
                else
                    tr[i] = ++rank;
            }

            int ind[] = new int[n];
            for(int i=0;i<n;i++){
                temp[i].rank = tr[i];
                ind[temp[i].value] = i;
            }
            for(int i=0;i<n;i++){
                if(temp[i].value + k/2 >= n)
                    temp[i].nextRank = -1;
                else
                    temp[i].nextRank = temp[ind[temp[i].value + k/2]].rank;
            }
            Arrays.sort(temp,cc);
        }

        int suffixArray[] = new int[n];

        for(int i=0;i<n;i++)
            suffixArray[i] = temp[i].value;
        return suffixArray;
    }

    public static int[] getLCP(int[] suffixArray,String str){
        int n = str.length();
        int rank[] = new int[n];

        for(int i=0;i<n;i++)
            rank[suffixArray[i]] = i;

        int lcp[] = new int[n];
        for(int i=0,k=0;i<n;i++){
            int v = rank[i];
            if(v==0)    continue;
            v--;
            v = suffixArray[v];
            while((i+k)<n && (v+k)<n && str.charAt(i+k)==str.charAt(v+k)){
                k++;
            }
            lcp[rank[i]] = k;
            k = k==0?0:k-1;
        }
        return lcp;
    }

    public static int findCeling(long[] arr,long k,int s,int e){
        if(k<arr[s]) return s;
        if(k>arr[e]) return -1;
        int mid = (s+e)/2;
        if(arr[mid]==k)
            return mid;
        if(arr[mid]<k){
            if(mid+1<=e && arr[mid+1]>k)
                return mid+1;
            else    
            return findCeling(arr,k,mid+1,e);
        }
        else{
            if(mid-1>=s && arr[mid-1]<k)
                return mid;
            else    
                return findCeling(arr,k,s,mid-1);
        }
    }
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your    class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int ii=0;ii<t;ii++){
            String str = sc.next();
            int sa[] = getSuffixArray(str);
            int lcp[] = getLCP(sa,str);
            int n = str.length();
            long range[] = new long[n];
            for(int i=0;i<n;i++){
                long len = (long)(n-sa[i]);
                range[i] = (long)(len*(len+1)/2)-(long)(lcp[i]*(lcp[i]+1)/2);
            }
            long k = sc.nextLong();
            for(int i=0;i<n;i++){
                int s = sa[i];
                int lc = lcp[i];
                if(range[i]>=k){
                    int len = 1+lc;
                    while(k>len){
                        k -= len;
                        len++;
                    }
                    System.out.println(str.charAt(s+(int)k-1));
                    break;
                }
                else
                    k -= range[i];
            }
        }
    }
}
