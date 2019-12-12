import java.util.Scanner;


public class Floyd {

    private static int S[][];  //Adjacent matrix
    private static int MAX = 10000000;

    private static void floyd(int S[][], int n){
        for(int k=1; k<=n; k++)
            for(int i=1; i<=n; i++)
                for(int j=1; j<=n; j++){
                    if (i==j) continue;
                    if (S[i][k]>=0 && S[k][j]>=0 && S[i][j] > S[i][k]+S[k][j])
                        S[i][j] = S[i][k]+S[k][j];
                }
    }

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int e = in.nextInt();

        S = new int[n+1][n+1];
        for (int i=1;i<=n;i++){
            for (int j=1;j<=n;j++) {
                S[i][j] = MAX;
            }
            S[i][i] = 0;
        }

        for (int i=1;i<=e;i++){
            int x = in.nextInt();
            int y =in.nextInt();
            int r = in.nextInt();
            S[x][y] = r;
        }

        Floyd.floyd(S,n);

        int q = in.nextInt();

        for (int i=1;i<=q;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            if(S[a][b]< MAX){
                System.out.println(S[a][b]);
            }
            else System.out.println(-1);
        }
        in.close();
    }

}
