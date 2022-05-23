
/*
어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자
*/
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    String c=a.nextLine();
	    String[] arr=c.split(":");
		System.out.printf("%s:%s",arr[0],arr[1]);
		a.close();
	}
}

