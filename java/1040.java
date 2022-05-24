/*
입력된 정수의 부호를 바꿔 출력해보자.
단, -2147483647 ~ +2147483647 범위의 정수가 입력된다.
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		long k=a.nextLong();
		System.out.print(-k);
		a.close();
	}
}

