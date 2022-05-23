
/*
2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.

*/
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    char num1=a.next().charAt(0);
	    char num2=a.next().charAt(0);	    
		System.out.print(num2+" "+num1);
		a.close();
	}
}
