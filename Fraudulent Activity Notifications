import java.util.Scanner;

public class FraudulentActivityNotifications {
    private static final int MAX_EXPENDITURE = 200;

    private static double getMedian(int[] countSort, int d)
    {
        int cursor = 0;
        int left = -1;
        int right = -1;
        double median = 0;

        for (int e = 0; e <= MAX_EXPENDITURE; e++) {
            cursor += countSort[e];
            if (d % 2 == 1) {
                // Odd -> Pick middle one for median
                if (cursor >= d / 2 + 1) {
                    median = e;
                    break;
                }
            } else {
                // Even -> Pick average of two middle values for median
                if (cursor == d / 2) {
                    left = e;
                }

                if (cursor > d / 2 && left != -1) {
                    right = e;
                    median = ((left + right) / 2.0);
                    break;
                }

                if (cursor > d / 2 && left == -1) {
                    median = e;
                    break;
                }
            }

        }
        return  median;
    }
    private static int solve(int[] arr, int n, int d) {
        int notifications = 0;
        int[] countSort = new int[MAX_EXPENDITURE + 1];

        // Add the first d expenditures to the countSort array.
        for (int i = 0; i < d; i++) {
            countSort[arr[i]] = countSort[arr[i]] + 1;
        }

        for (int i = d; i < n; i++) {
            int currentAmount = arr[i];

            double median = getMedian(countSort, d);

            if (currentAmount >= 2 * median) {
                notifications++;
            }

            // Update countSort: slide window 1 index to right
            countSort[arr[i - d]] = countSort[arr[i - d]] - 1;
            countSort[arr[i]] = countSort[arr[i]] + 1;
        }


        return notifications;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int d = scanner.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        System.out.println(solve(arr, n, d));
    }
}
