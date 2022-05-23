
/*
년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.
*/
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    String c=a.nextLine();
	    String[] arr=c.split("\\.");
	    int year=Integer.parseInt(arr[0]);
	    int month=Integer.parseInt(arr[1]);
	    int day=Integer.parseInt(arr[2]);
	  
		System.out.printf("%04d.%02d.%02d",year,month,day);
		a.close();
	}
}

