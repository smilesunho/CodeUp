/*
영문자 1개를 입력받아 그 다음 문자를 출력해보자.

영문자 'A'의 다음 문자는 'B'이고, 영문자 '0'의 다음 문자는 '1'이다.
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		char k=a.nextLine().charAt(0);
		int b=k+1;
		char c=(char)b;
		System.out.print(c);
		a.close();
	}
}

