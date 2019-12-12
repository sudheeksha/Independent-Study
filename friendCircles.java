class unionFind{
    int[] parent;
    int circleSize;
    
    public unionFind(int size, int circleSize){
        this.circleSize = circleSize;
        parent = new int[size];
        
        for(int i = 0; i < size; i++){
            parent[i] = i;
        }
    }
    
    public int find(int p){
        if (p==parent[p])
            return p;
        return parent[p] = find(parent[p]);
    }
    
    public void union(int p, int q){
        int aParent = find(p);
        int bParent = find(q);

        if (aParent!=bParent){
            parent[aParent] = bParent;
            circleSize--;
        }
    }
    
    public int getCircleSize(){
        return circleSize;
    }
    
}

class Solution {
    public int findCircleNum(int[][] M) {
        int m = M.length;
        int n = M[0].length;
        unionFind uf = new unionFind(m*n, m);
        for (int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(M[i][j] == 1 && i!=j){
                    uf.union(i,j);
                }
            }
        }
        return uf.getCircleSize();
    }
}
