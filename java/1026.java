
/*
입력되는 시:분:초 에서 분만 출력해보자.
*/

import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    String c=a.nextLine();
	    String[] arr=c.split(":");
	    int k=Integer.parseInt(arr[1]);
		System.out.print(k);
		a.close();
	}
}

