/*
8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		String c =a.nextLine();
		int n=Integer.parseInt(c,8);
	    System.out.print(n);
		a.close();
	}
}

