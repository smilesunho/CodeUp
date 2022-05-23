
/*
정수(int) 2개를 입력받아 그대로 출력해보자.

*/
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    int num1=a.nextInt();
	    int num2=a.nextInt();	    
		System.out.print(num1+" "+num2);
		a.close();
	}
}
