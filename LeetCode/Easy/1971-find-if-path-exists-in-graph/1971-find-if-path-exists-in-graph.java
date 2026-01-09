class UnionFind{
    int[] parent;
    int[] weight;
    int count;
    public UnionFind(int n){
        this.parent = new int[n];
        this.weight = new int[n];
        this.count = n;
        for (int i = 0; i < n; i++){
            this.parent[i] = i;
            this.weight[i] = 1;
        }
    }

    public int find(int x){
        if (this.parent[x] == x) return x;
        this.parent[x] = find(this.parent[x]);
        return this.parent[x];
    }

    public void union(int x, int y){
        int leaderX = find(x);
        int leaderY = find(y);
        if (leaderX == leaderY) return;
        int weightX = this.weight[leaderX];
        int weightY = this.weight[leaderY];
        if (weightX < weightY){
            this.parent[leaderX] = leaderY;
            this.weight[leaderY] += weightX;
        }
        else{
            this.parent[leaderY] = leaderX;
            this.weight[leaderX] += weightY;
        }
    }

    public boolean inSameSet(int x, int y){
        int leaderX = find(x);
        int leaderY = find(y);
        return leaderX == leaderY;
    }
    
}


class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        
        UnionFind uf = new UnionFind(n);
        for (int i = 0; i < edges.length; i++){
            uf.union(edges[i][0], edges[i][1]);
        }
        return uf.inSameSet(source, destination);















    }
}