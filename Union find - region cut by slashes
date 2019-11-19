class unionFind{
    int[] parent;
    int[] rank;
    int size;
    
    public unionFind(int size){
        this.size = size;
        rank = new int[size];
        parent = new int[size];
        
        for(int i = 0; i < size; i++){
        // Initially, each thing points to itself and the rank is 1.
            rank[i] = 1;
            parent[i] = i;
        }
    }
    
    public int find(int p){
    //Finding the parent recursively.
        if (p==parent[p])
            return p;
        return parent[p] = find(parent[p]);
    }
    
    public void union(int p, int q){
    //Joining two sets.
        int aParent = find(p);
        int bParent = find(q);
        if(rank[aParent] < rank[bParent]){
        //Check the rank and assign the highest ranker as the parent
            parent[aParent] = bParent;
            rank[bParent] += rank[aParent];
        }else if(rank[aParent] > rank[bParent]){
            parent[bParent] = aParent;
            rank[aParent] += rank[bParent];
        }else{
            parent[bParent] = aParent;
            rank[aParent] += rank[bParent];
        }
    }
    
}
class Solution {
    public int regionsBySlashes(String[] grid) {
        int N = grid.length;
        unionFind uf = new unionFind(4 * N * N);
        for (int r = 0; r < N; ++r)
            for (int c = 0; c < N; ++c) {
                int root = 4 * (r * N + c);
                char val = grid[r].charAt(c);
                if (val != '\\') {
                    uf.union(root + 0, root + 1);
                    uf.union(root + 2, root + 3);
                }
                if (val != '/') {
                    uf.union(root + 0, root + 2);
                    uf.union(root + 1, root + 3);
                }

                // north south
                if (r + 1 < N)
                    uf.union(root + 3, (root + 4 * N) + 0);
                if (r - 1 >= 0)
                    uf.union(root + 0, (root - 4 * N) + 3);
                // east west
                if (c + 1 < N)
                    uf.union(root + 2, (root + 4) + 1);
                if (c - 1 >= 0)
                    uf.union(root + 1, (root - 4) + 2);
            }

        int result = 0;
        for (int x = 0; x < 4 * N * N; ++x) {
            if (uf.find(x) == x)
                result++;
        }

        return result;
    }
}
