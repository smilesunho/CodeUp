
/*
실수 1개를 입력받아 그대로 출력해보자.
(단, 입력되는 실수의 범위는 +- 1.7*10-308 ~ +- 1.7*10308 이다.)
*/


import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    double c=a.nextDouble();
	    String str=String.format("%.11f",c);	
	    System.out.println(str);
		a.close();
	}
}
