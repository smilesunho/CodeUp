
/*
영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		char c =a.nextLine().charAt(0);
		int n=(int) c;
	    System.out.print(n);
		a.close();
	}
}

