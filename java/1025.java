
/*
다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
*/
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		List listAdd=new ArrayList();
		Scanner a = new Scanner(System.in);
	    String c=a.nextLine();
	    for(int i=0; i<c.length();i++) {
	        char t=c.charAt(i);
	    	int k=Character.getNumericValue(t);
	    	listAdd.add(k);	
	    }
	    int i1=(int) listAdd.get(0)*10000;
	    int i2=(int) listAdd.get(1)*1000;
	    int i3=(int) listAdd.get(2)*100;
	    int i4=(int) listAdd.get(3)*10;
	    int i5=(int) listAdd.get(4);
	    System.out.println("["+i1+"]");
	    System.out.println("["+i2+"]");
	    System.out.println("["+i3+"]");
	    System.out.println("["+i4+"]");
	    System.out.println("["+i5+"]");
	    a.close();
	}
}
