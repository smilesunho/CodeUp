
/*
실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
*/
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    String c=a.nextLine();
	    String[]arr=c.split("\\.");
	    int first=Integer.parseInt(arr[0]);
	    int last=Integer.parseInt(arr[1]);
		System.out.println(first);
		System.out.print(last);
		a.close();
	}
}
