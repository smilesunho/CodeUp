/*
정수 2개를 입력받아 합을 출력해보자.
단, 입력되는 정수는 -2147483648 ~ +2147483648 이다.
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		long k=a.nextLong();
		long j=a.nextLong();
		System.out.print(k+j);
		a.close();
	}
}

