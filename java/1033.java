/*
10진수를 입력받아 16진수(hexadecimal)로 대문자로 출력해보자.
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    int c=a.nextInt();
	    System.out.printf("%X",c);
		a.close();
	}
}

