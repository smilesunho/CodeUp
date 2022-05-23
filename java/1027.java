/*
년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.

년월일(yyyy.mm.dd)를 입력받아,

일월년(dd-mm-yyyy)로 출력해보자.

(단, 한 자리 일/월은 0을 붙여 두자리로, 년도도 0을 붙여 네자리로 출력한다.) 
*/

import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
	    String c=a.nextLine();
	    String[] arr=c.split("\\.");
	    int k0=Integer.parseInt(arr[0]);
	    int k1=Integer.parseInt(arr[1]);
	    int k2=Integer.parseInt(arr[2]);	    
		System.out.printf("%02d-%02d-%04d",k2,k1,k0);		
		a.close();
	}
}
