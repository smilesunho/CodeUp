
/*
10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
단, 0 ~ 255 범위의 정수만 입력된다.
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		int c =a.nextInt();
		char b=(char) c;
	    System.out.print(b);
		a.close();
	}
}

