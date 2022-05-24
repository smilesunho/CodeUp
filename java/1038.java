
/*
정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
(단, 입력되는 정수는 -1073741824 ~ 1073741824 이다.)
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		double k=a.nextInt();
		double j=a.nextInt();
		System.out.printf("%.0f",k+j);
		
	}
}

