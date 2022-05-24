/*
10진수를 입력받아 8진수(octal)로 출력해보자.
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    int c=a.nextInt();
	    System.out.printf("%o",c);
		a.close();
	}
}

