
/*
정수 1개를 입력받아 그대로 출력해보자.
(단, 입력되는 정수의 범위는 0 ~ 4,294,967,295 이다.)
*/

import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    long c=a.nextLong();
	    System.out.println(c);
		a.close();
	}
}

